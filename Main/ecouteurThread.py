#!/usr/bin/env python
# coding: utf-8
import base64
import socket
import threading
import struct
from base64 import decodestring
from PIL import Image
from base64 import decodestring
import datetime

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))
        self.numero = 1

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))
        received_chunks = []
        buf_size = 3447429
        size = buf_size
        remaining = size
        while remaining > 0:
            received = self.clientsocket.recv(min(remaining, buf_size))
            if not received:
                raise Exception('unexcepted EOF')
            received_chunks.append(received)
            remaining -= len(received)
        res = (b''.join(received_chunks))
        print (res)
        now = datetime.datetime.now()
        filename = str(('%s,%s'%(now.minute,now.second)))+".png"
        self.numero = self.numero+1
        #print ("self.numero : "),self.numero
        #base64.b64decode(bytes(res, 'utf-8'))
        imgdata = decode_base64(res)
        with open(filename, 'wb') as f:
            f.write(imgdata)


#TODO : METTRRE LE I HORS DE LA FONCTION;
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 5001))

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()