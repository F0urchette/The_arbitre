#!/usr/bin/python
import socket

import cv2
import numpy

TCP_IP = '192.168.0.50'
TCP_PORT = 5001

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

frame = cv2.imread("cgm.jpg")

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
result, imgencode = cv2.imencode('.jpg', frame, encode_param)
data = numpy.array(imgencode)
stringData = data.tostring()


sock.send( stringData )
sock.close()

decimg=cv2.imdecode(data,1)
# cv2.imshow('CLIENT',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows()