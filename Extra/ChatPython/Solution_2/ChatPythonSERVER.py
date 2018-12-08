#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://www.geeksforgeeks.org/simple-chat-room-using-python/

# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from thread import *
  
"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Si le port a ete utilise par une autre session precedente , il sera reutilisable grace a cette ligne.

#Verifie si il y a eu le nombre coorecte d'argument saisi par l'utilisateur 
# checks whether sufficient arguments have been provided 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address and port number.")
    print ("Pour que le tout fonctionne de maniere correcte, il faut saisir : le Script Python, l'Adresse IP et le Port du Serveur.")
    exit() 
  
# takes the first argument from command prompt as IP address 
IP_address = str(sys.argv[1]) 
  
# takes second argument from command prompt as port number 
Port = int(sys.argv[2]) 
  
""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
#Rattachement de la Socket a une adresse IP et un PORT
server.bind((IP_address, Port)) 
  
""" 
listens for 113 active connections. This number can be 
increased as per convenience. 
"""
#Le Serveur peut avoir 113 communications active en simulatanee
server.listen(113) 
  
list_of_clients = [] 
  
def clientthread(conn, addr): 
    #Envoie a tout les client qui ce connecte ce message
    # sends a message to the client whose user object is conn 
    conn.send("Bienvenue dans ce Salon!") 
  
    while True: 
            try: 
                message = conn.recv(2048) #Le Message recu de 2048 octets
                if message: 
  
                    """prints the message and address of the 
                    user who just sent the message on the server 
                    terminal"""
                    print ("<" + addr[0] + "> " + message)              #Affichage de l'adresse IP de l'utilisateur qui ecrit et de son message
  
                    # Calls broadcast function to send message to all   #Envoie un message a tout les client quand le Serveur decide d'envoyer un message
                    message_to_send = "<" + addr[0] + "> " + message    #Affichage de l'adresse IP et du message dans la console
                    broadcast(message_to_send, conn)                    #Envoie du Message a tout les clients dans le chat
  
                else: 
                    """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                    remove(conn)                                        #Si il y a eu un probleme durant une transmission , la connection s'arrete
  
            except: 
                continue
  
"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
#Fonctionnalite permettant d'envoyer un message a tout les clients
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  
"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""
#Fonctionnalite permettant d'arreter la transmission
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 
  
    """Accepts a connection request and stores two parameters,  
    conn which is a socket object for that user, and addr  
    which contains the IP address of the client that just  
    connected"""
    #Accepte la connexion d'un Nouvel utilisateur
    conn, addr = server.accept() 
  
    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    #Maintient une liste de client pour un envoie en BROADCAST d'un message eventuel du SERVEUR
    list_of_clients.append(conn) 

    #Quand un nouvel utilisateur ce connecte , on peut voir dans la console son addresse IP et un message qui indique son etat de connexion
    # prints the address of the user that just connected 
    print (addr[0] + " connected")
  
    # creates and individual thread for every user  
    # that connects 
    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close() 
