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
import cv2
from io import BytesIO

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
        while True:
            received = self.clientsocket.recv(1024)
            if not received:
                break
            received_chunks.append(received)
            #remaining -= len(received)
        res = (b''.join(received_chunks))
        print("----------------------------------")
        print (res)
        print("----------------------------------")
        now = datetime.datetime.now()
        print ("Nom fichier : ")
        filename = str(('%s_h_%s_m_%s_s'%(now.hour,now.minute,now.second)))+".jpeg"
        print (filename)
        print("----------------------------------")
        print("Type de res:")
        print(type(res))
        print("----------------------------------")
        #if b'==\n' not in res:
            #res = res.decode('utf-8').strip()
        #res += "=" * ((4 - len(res) % 4) % 4)
        outputdata = decode_base64(res)
        #print(outputdata)
        with open(filename, 'wb') as f:
            f.write(outputdata)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 5001))

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    try:
        missing_padding = len(data) % 4
        if missing_padding != 0:
            data += b'='* (4 - missing_padding)
        return base64.decodestring(str(data))
    except:
        return base64.urlsafe_b64decode(str(data))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    #newthread.daemon = True
    newthread.start()