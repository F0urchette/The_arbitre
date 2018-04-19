#!/usr/bin/python
import socket

import cv2
import numpy


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def recv_basic(the_socket):
    total_data=[]
    while True:
        data = the_socket.recv(8192)
        if not data: break
        total_data.append(data)
    return b''.join(total_data)


TCP_IP = 'localhost'
TCP_PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)


while 1:
    conn, addr = s.accept()

    stringData = recv_basic(conn)
    data = numpy.fromstring(stringData, dtype='uint8')

    decimg=cv2.imdecode(data,1)
    print("image recue")
    cv2.imwrite('resultat.jpg', decimg)
    cv2.imshow('SERVER',decimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

s.close()