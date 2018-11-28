# j'importe le module
import socket

# je cree la socket TCP
sck  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# je me connect
Host = '127.0.0.1'
Port = 139
sck.connect((Host,Port))

print "Vous etes connect !"

# boucle pour reste connecte
while (sck.connect):

    # le client ecrit
    donnee_envoi = raw_input(" >>> ")

    # ils envoi les donnees
    sck.send(donnee_envoi)

    # ils affiche (esthetique)
    print " >>> " + donnee_envoi
