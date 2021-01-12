import asyncio


async def _handle_client(client_reader, client_writer):
    nickname = await client_reader.readline()
    nickname = nickname.decode('utf-8').strip()
    print(f'*** {nickname} a rejoint la discussion')

    while True:
        msg = await client_reader.readline()
        msg = msg.decode('utf-8')
        if not msg or msg[:5] == '/quit':
            break
        print(f'<{nickname}> {msg.strip()}')

    print(f'*** {nickname} a quitté la discussion')


def main(port=4240):
    loop = asyncio.get_event_loop()
    coro = asyncio.streams.start_server(_handle_client, '', port, loop=loop)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
