import asyncio

messages = []
new_message = asyncio.Condition()

def _send_all(msg):
    print(msg)
    with (yield from new_message):
        messages.append(msg + '\n')
        new_message.notify_all()


@asyncio.coroutine
def _handle_rclient(client_reader, client_writer):
    nickname = yield from client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    if not nickname or not nickname.strip():
        return
    yield from _send_all('*** {} a rejoint la discussion'.format(nickname))

    while True:
        msg = yield from client_reader.readline()
        msg = msg.decode('utf-8')
        if not msg or msg[:5] == '/quit':
            break
        if not msg.strip():
            continue
        yield from _send_all('<{}> {}'.format(nickname, msg.strip()))

    yield from _send_all('*** {} a quitté la discussion'.format(nickname))

@asyncio.coroutine
def _handle_wclient(client_reader, client_writer):
    i = len(messages)
    while True:
        with (yield from new_message):
            yield from new_message.wait()
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
