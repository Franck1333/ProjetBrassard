#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://www.geeksforgeeks.org/simple-chat-room-using-python/

# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
  
"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address and port number.")
    print ("Pour que le tout fonctionne de maniere correcte, il faut saisir : le Script Python, l'Adresse IP et le Port du Serveur.")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2])
#Connection au Serveur
server.connect((IP_address, Port))

PSEUDO = raw_input("Quel est ton Pseudo?")
print("Coucou ", PSEUDO)
  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets: 
        if socks == server:
            #Message a emettre
            message = socks.recv(2048) 
            print (message) 
        else: 
            message = sys.stdin.readline()  #Message a Emettre 
            server.send(PSEUDO +" a dit : "+ message)            #Emission du Message
            sys.stdout.write(PSEUDO + " : ")       #Message d'indication du SUJET dans la console
            sys.stdout.write(message)       #Affichage dans la console du/des Messages Emis
            sys.stdout.flush() 
server.close() 
