#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import base64
import datetime
import socket
import threading
import re
import math
from Modele import Robot, Victime, Hopital
import cv2
import numpy
from PIL import Image
import io
import codecs
class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        print(a)
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

        image = decode_base64(res)
        qrCodes = findQrCodes(image)

        # On entre la position des victimes et des hopitaux au début de la partie
        if not setup :
            # Passe la variable setup a True
            setupVictimeEtHopitaux(qrCodes)

        # On traite tous les qrCodes trouves sur l'image
        for qrCode in qrCodes :
            # Renvoie l'id inscrit dans le qrCode et un booleen selon s'il s'agit d'un robot ou non
            id, isRobot = verifQrCode(qrCode)

            # On traite donc un robot
            if isRobot :
                # On met a jour la position du robot dans la BD
                updatePosRobot(id, qrCode)

                # On verifie si le robot a quitte la ligne et on lui applique un malus si c'est le cas
                malusLigne(id, image)

                # On compte les points si le robot est pret d'un hopital, récupere une victime, tout en verifiant si la capacite du robot le permet
                compterPoints(id)

                # S'il n'y a plus de victime on arrete le serveur et on sauvegarde les scores
                if isPlusDeVictime() :
                    fin = True
                    printScore()

        fh = open(filename, "wb")
        fh.write(image)
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

def ajouter(qrCode) :
    id = str(lireIdQrCode(qrCode))
    if re.match("\d", id) :
        ajouterRobot(id, lirePositionQrCode(qrCode))
    elif re.match("[a-z]", id) :
        ajouterVictime(id, lireTypeQrCode(qrCode), lirePositionQrCode(qrCode))
    elif re.match("[A-Z]", id) :
        ajouterHopital(id, lireTypeQrCode(qrCode), lirePositionQrCode(qrCode))
    else :
        None

def ajouterRobot(id, position) :
    id = str(id)
    if id in robots :
        robot = robots[id]
        robot.majPosition(position)
    else :
        robot = Robot(id, position)
        robots[id] = robot

def ajouterVictime(id, type, position) :
    id = str(id)
    if id not in victimes:
        victime = Victime(id, type, position)
        victimes[id] = victime

def ajouterHopital() :
    id = str(id)
    if id not in hopitaux:
        hopital = Hopital(id, type, position)
        hopitaux[id] = hopital

def lireIdQrCode(qrCode) :
    return ""

def lireTypeQrCode(qrCode) :
    return 0

def lirePositionQrCode(qrCode) :
    return (0, 0)

def setupVictimeEtHopitaux(qrCodes) :
    for qrCode in qrCodes :
        ajouter(qrCode)
    setup = True

def verifQrCode(qrCode) :
    id = lireIdQrCode(qrCode)
    isRobot = False
    if re.match("\d", id) :
        isRobot = True
    return id, isRobot

def updatePosRobot(id, qrCode) :
    id = str(id)
    ajouterRobot(id, lirePositionQrCode(qrCode))

def isPlusDeVictime() :
    for victime in victimes :
        if victime.isDisponible() :
            return False
    return True

def malusLigne(id, image) :
    id = str(id)

    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Threshold it so it becomes binary
    ret, thresh = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)
    # You need to choose 4 or 8 for connectivity type
    connectivity = 4
    output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    num_labels -= 1

    if num_labels != 1 :
        robot = robots[id]
        robot.ajouterMalusLigne()

def compterPoints(id) :
    id = str(id)
    robot = robots[id]
    isProche, victime = isProcheDeVictime(robot)
    if isProche :
        if victime.isDisponible() :
            if robot.isPlaceDisponible() :
                type = victime.getType()
                victime.setNonDisponible()
                robot.transporter(type)
    else
        isProche, hopital = isProcheDeHopital(robot)
        if isProche:
            type = hopital.getType()
            robot.sauver(type)

def distance2Points(a, b) :
    p1 = pow(b[0] - a[0], 2)
    p2 = pow(b[1] - a[1], 2)
    return math.sqrt(p1 + p2)

def isProcheDeVictime(robot) :
    for victime in victimes :
        d = distance2Points(robot.getPosition(), victime.getPosition())
        if d <= 5 :
            return True, victime
    return False, None

def isProcheDeHopital(robot) :
    for hopital in hopitaux :
        d = distance2Points(robot.getPosition(), hopital.getPosition())
        if d <= 5 :
            return True, hopital
    return False, None

def printScore() :


fin = False
setup = False
robots = dict()
victimes = dict()
hopitaux = dict()

while not fin:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    #newthread.daemon = True
    newthread.start()