#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import base64
import datetime
import socket
import threading
import cv2
import numpy
from PIL import Image
import io
import codecs
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

        """
        print(len(res))
        taille = len(res)
        print(type(taille))
        taille = taille/2
        print(taille)
        outputdata1 = res[:2000000]
        outputdata2 = res[2000000:]
        """
        #res1 = decode_base64(outputdata1)
        #res2 = decode_base64(outputdata2)

        #outputdata = res1 + res2
        """"
        file_like = cStringIO.StringIO(data)

        img = PIL.Image.open(file_like)
        img.show()"""

        #outputdata = decode_base64(res)

        #image = Image.open(io.BytesIO(res))
        #image.show()


        """"
        #data = numpy.fromstring(res, dtype='uint8')
        #decimg = cv2.imdecode(data, 1)
        #cv2.imwrite(filename, decimg)
        #cv2.imshow('SERVER', decimg)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #print(outputdata)
         """
        #image = Image.frombytes('RGBA', (1500,1500), res, 'raw')
        #image.show()


        fh = open(filename, "wb")
        fh.write(decode_base64(res))
        fh.close()

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 5001))

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """

    missing_padding = len(data) % 4
    if missing_padding == 3:
        data += b'A=='
    elif missing_padding == 1 or missing_padding == 2:
        data += b'=' * missing_padding
    #if missing_padding != 0:
        #data += b'=' * (4 - missing_padding)
    return base64.b64decode(data)

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    #newthread.daemon = True
    newthread.start()