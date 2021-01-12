import asyncio

LINES = (
    "Bravo !",
    "Tu as réussi...",
    "...à afficher plusieurs lignes !"
    ""
)


async def _handle_client(client_reader, client_writer):
    for l in LINES:
        client_writer.write(bytes(l + '\n', encoding='utf-8'))


def main(port=2000):
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
