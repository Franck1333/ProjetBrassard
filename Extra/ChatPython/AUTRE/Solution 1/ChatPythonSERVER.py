# j'importe le module
import socket
#AUTRE
import select 
import sys 
from thread import *

# je cree la socket TCP
sck =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# je bind la socket
Host = ''
Port = 139
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind((Host,Port))

# je la met en ecoute 
sck.listen(213)

# jaccepte le client
client, ip = sck.accept()

print ("Nouvelle connexion : ", ip)

#list_of_clients = []

# tant que l'ont est connecte
while (sck.connect):

    # donnee_recu gere les donnees recu (max 1024 octees)
    donnee_recu = client.recv(2048).decode("utf-8")

    # Si ont ne recoi rien on attend afin deviter de faire morfle le processeur
    if not donnee_recu : break
    
    # Sinon j'affiche les donnees recu
    else : print (" >>> ", donnee_recu)
