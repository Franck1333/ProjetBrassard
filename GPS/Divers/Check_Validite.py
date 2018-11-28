#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial
import time
import os
import sys

from Recuperation_Determination import *
from Recuperation_Determination import parse_GPRMC
#from Recuperation_Determination import ouverture_serie
from Recuperation_Determination import lecture_return_serie

try :
    from Tkinter import * #Python Version 2
    pass
except:
    from tkinter import * #Python Version 3


fenetre = Tk()


def GPS_test():

    #while 1:    #Boucle infinie de Démonstration

    Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere, = lecture_return_serie() #Récuperation des variables depuis le fichier Python "Recuperation_Determination"


    #Validite = "V" #Valeur de TEST

    global GPS
    global GPSErreur

    if Validite == "V":

        GPSErreur = Toplevel()

        Label_Annonce_GPSErreur = Label(GPSErreur,text="Malheureusement, Nous ne captons pas correctement le Signal G.P.S , déplacez vous ;=)").pack() 

        Label_ShowValue_GPSErreur = Label(GPSErreur, text=Validite).pack()

        print("La Trame recu n'est pas Valide // Validite = V :", Validite)

        Button(GPSErreur, text="Fermer", command=GPSErreur.destroy).pack()


    else : #if Validite == "A":
        GPS=Toplevel()

        Label_Annonce_GPS = Label(GPS,text="Nous captons correctement le Signal GPS, le Programme pourras continuer comme prévue").pack()

        Label_ShowValue_GPS = Label(GPS,text=Validite).pack()
        
        print("La Trame recu est Valide // Validite = A :", Validite)

        Button(GPS, text="Fermer", command=GPS.destroy).pack()

Button(fenetre, text="G.P.S_test", command=GPS_test).pack()
Button(fenetre, text="Fermer...", command=fenetre.quit).pack()


fenetre.mainloop()



#Ce petit programme permet de Tester la Validite d'une Trame GPS reçue est de savoir si elle est Accpeter ou Refuser
#Dans le cas ou elle serait Refuser, Une fenêtre dédiée s'ouvrira et indiquera que le Signal GPS reçue n'est pas Bon.
#Dans le cas contraire , Une Fenêtre tkinter dédiée s'ouvrira à son tour pour indiquer que le Signal GPS est Accepter et que le Programme continue son éxécution.




                #Par ce petit programme, je montre comment récupere les valeurs GPS de manière plus proche de la source qu'auparavant de cette manière en utilisant la Fonction "lecture_return_serie()" définie dans Recuperation_Determination.py .
                    
                #-------------------------------lecture_return_serie()-------------------------------
                #def lecture_return_serie():
                #    global gpsData
                #    gpsData = None
                #    while gpsData == None :                                #Tant que 'gpsData' est non définie alors on capture les information provenant du port serie et on retourne le resultat.
                #
                #        ser = serial.Serial('/dev/ttyACM0',4800,timeout=0) #Open Serial port Configure le Recepteur G.P.S
                #
                #        data = ser.readline()                              #Lecture de la liason serie Ligne par Ligne
                #    
                #        if "$GPRMC" in data:                               #SELECTION DE LA LIGNE GPRMC  
                #             gpsData = parse_GPRMC(data)                   #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
                #             
                #    return gpsData
                #-------------------------------lecture_return_serie()-------------------------------
