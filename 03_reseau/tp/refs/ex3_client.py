#!/usr/bin/env python3

import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tcpsock.connect(("127.0.0.1", 2001))
rfile = tcpsock.makefile("r", encoding="utf-8")

while True:
    line = rfile.readline()
    if line == '\n':
        break
    print(line, end='')

rfile.close()
tcpsock.shutdown(socket.SHUT_RDWR)
tcpsock.close()
