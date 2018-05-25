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



src = cv2.imread("test5.jpg")
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# Threshold it so it becomes binary
ret, thresh = cv2.threshold(src,127,255,cv2.THRESH_BINARY)
cv2.imshow('SERVER',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
# You need to choose 4 or 8 for connectivity type
connectivity = 4
output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
# Get the results
# The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix
stats = output[2]
# The fourth cell is the centroid matrix
centroids = output[3]
print(num_labels)

