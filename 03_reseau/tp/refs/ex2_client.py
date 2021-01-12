#!/usr/bin/env python3

import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# Modifier le port en 4241 pour la partie finale `client_reception`
tcpsock.connect(("127.0.0.1", 2000))
rfile = tcpsock.makefile("r", encoding="utf-8")

while True:
    print(rfile.readline())

rfile.close()
tcpsock.shutdown(socket.SHUT_RDWR)
tcpsock.close()
