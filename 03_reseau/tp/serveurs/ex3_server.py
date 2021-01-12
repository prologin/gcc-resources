import asyncio
from random import choice, randint

HEADER = "Les lignes qui suivent contiennent un nombre indeterminé de mots."
LINES = ('antepenult', 'rattlingness', 'pointillist', 'zinco', 'diplohedron',
        'improof', 'archibenthos', 'stainlessness', 'overgrace', 'referrer',
        'autoplasty', 'flatus', 'chamaecranial', 'anticentralization',
        'overhurry', 'synodalian', 'pentactinal', 'aliturgical',
        'morphometrical', 'supinely', 'virology', 'disappointingly',
        'aortoptosis', 'fasciately', 'shelteringly', 'Chequers', 'pilaster',
        'predisponent', 'wastingly', 'unactive')


async def _handle_client(client_reader, client_writer):
    client_writer.write(bytes(HEADER + '\n', encoding='utf-8'))
    for l in [choice(LINES) for _ in range(randint(2, len(LINES)))]:
        client_writer.write(bytes(l + "\n", encoding='utf-8'))
    client_writer.write(bytes('\n', encoding='utf-8'))


def main(port=2001):
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
