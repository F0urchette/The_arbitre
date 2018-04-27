#!/usr/bin/env python
# coding: utf-8

import socket
import threading
from PIL import Image
import io


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))

        bytes_data = self.clientsocket.recv(2048)
        part = bytes_data
        i = 1
        print("Part #", str(i))
        while part.decode() != 'Sent':
            part = self.clientsocket.recv(1024)
            bytes_data += part
            i += 1
            print("Part #", str(i))
        img = Image.frombytes('RGB', (1366, 768), bytes_data)
        img.save('newimg.jpg')

        print("Client déconnecté...")


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 5001))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()