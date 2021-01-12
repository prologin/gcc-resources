import asyncio
import time

messages = []
new_message = asyncio.Condition()

# Contains list of (ip, pseudo, time_spam)
spammers = []

# Rate limit = `RATE_MESSAGE` / `RATE_SECONDS`
RATE_MESSAGE = 10
RATE_SECONDS = 1


async def _send_all(msg):
    print(msg)
    async with new_message:
        messages.append(msg)
        new_message.notify_all()


async def _handle_rclient(client_reader, client_writer):
    # Get peername to send spam warning
    socket = client_writer.get_extra_info('socket')
    peername = None
    if socket is not None:
        peername = socket.getpeername()[0]

    # Get nickname
    nickname = await client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    await _send_all(f'*** {nickname} a rejoint la discussion ({peername})')
    messages = 0
    last_time = time.time()

    while True:
        msg = await client_reader.readline()
        msg = msg.decode('utf-8')

        # empty message, discarding
        if (len(msg.strip()) == 0):
            continue

        # check if the client is a spammer
        if any(peername in spammer for spammer in spammers):
            current_time = time.time()
            (ip, pseudo, spam_time) = [(ip, pseudo, spam_time)
                                       for ip, pseudo, spam_time in spammers
                                       if ip == peername][0]
            # Spam limitation is over
            if (current_time >= spam_time + RATE_SECONDS):
                spammers.remove((ip, pseudo, spam_time))
            # Current limitation prevents to send messages
            else:
                continue

        # spam detection routine
        if messages == RATE_MESSAGE:
            current_time = time.time()
            if (current_time - last_time) < RATE_SECONDS:
                spammers.append((peername, nickname, current_time))
                print(f'{nickname} ({peername}) is spamming.')
                async with new_message:
                    # Notify to send a warning message to spammer
                    new_message.notify_all()
                continue
            messages = 0
            last_time = current_time
        messages += 1

        if not msg or msg[:5] == '/quit':
            break
        await _send_all(f'<{nickname}> {msg}')

    await _send_all(f'*** {nickname} a quitté la discussion')


async def _handle_wclient(client_reader, client_writer):
    i = len(messages)
    socket = client_writer.get_extra_info('socket')
    peername = None
    if socket is not None:
        peername = socket.getpeername()[0]

    spam_time = 0
    already_warned = 0

    while True:
        async with new_message:
            await new_message.wait()

            # Check if client is a spammer
            if any(peername in spammer for spammer in spammers):
                if spam_time > (time.time() + RATE_SECONDS):
                    # The client is not anymore restricted, reset flag
                    already_warned = 0

                # Send him a warning if it is the first time
                if not already_warned:
                    client_writer.write(bytes(
                        f"Spam détecté ! (Plus de {RATE_MESSAGE} messages"
                        f"en {RATE_SECONDS} secondes)\n",
                        encoding='utf-8'))
                    already_warned = 1
                    spam_time = time.time()

            for msg in messages[i:len(messages)]:
                client_writer.write(bytes(msg, encoding='utf-8'))
            i = len(messages)


def main(rport=4242, wport=4241):
    loop = asyncio.get_event_loop()
    rcoro = asyncio.streams.start_server(_handle_rclient, '', rport, loop=loop)
    wcoro = asyncio.streams.start_server(_handle_wclient, '', wport, loop=loop)
    rserver = loop.run_until_complete(rcoro)
    wserver = loop.run_until_complete(wcoro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    rserver.close()
    wserver.close()
    loop.run_until_complete(rserver.wait_closed())
    loop.run_until_complete(wserver.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
