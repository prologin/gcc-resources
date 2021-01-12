#!/usr/bin/env python3

import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
tcpsock.connect(("127.0.0.1", 2000))
rfile = tcpsock.makefile("r", encoding="utf-8")

print(rfile.readline())

rfile.close()
tcpsock.shutdown(socket.SHUT_RDWR)
tcpsock.close()
