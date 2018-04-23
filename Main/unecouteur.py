from socket import *

HOST = "192.168.0.50" #local host
PORT = 5001 #open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #how many connections can it receive at one time
conn, addr = s.accept() #accept the connection
print("Ecoute sur 192.168.0.50")
print ("Connecté : " , addr) #print the address of the person connected
i = 0
while True:
    data = conn.recv(1024) #how many bytes of data will the server receive
    if(repr(data) != "b''") :
        print ("Recu : ", repr(data))
    #reply = "Message recu, envoi d'une réponse.".encode() #server's reply to the client
    #conn.sendall(reply)
    #i = i+1
    del data
conn.close()