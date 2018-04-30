#!/usr/bin/env python
# coding: utf-8
import base64
import socket
import threading


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))
        bytes_data = self.clientsocket.recv(65536)
        print (bytes_data)
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(bytes_data))


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 5001))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()