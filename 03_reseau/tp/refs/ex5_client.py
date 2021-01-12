#!/usr/bin/env python3

import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# Modifier le port en 4242 pour la partie finale `client_envoi`
tcpsock.connect(("127.0.0.1", 4240))
wfile = tcpsock.makefile("w", encoding="utf-8")

pseudo = input("Entrez un pseudonyme : ")
wfile.write(pseudo + "\n")
wfile.flush()

while True:
    msg = input("> ")
    wfile.write(msg + '\n')
    wfile.flush()
    if msg == "/quit":
        break

wfile.close()
tcpsock.shutdown(socket.SHUT_RDWR)
tcpsock.close()
