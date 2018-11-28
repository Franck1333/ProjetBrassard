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

while 1:    #Boucle infinie de Démonstration

    Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere, = lecture_return_serie() #Récuperation des variables depuis le fichier Python "Recuperation_Determination"

    print("Voici les Coordonées reçu:")                                                 #Affichage d'un Message
    print(Decimal_latitude,Latitude_Hemisphere,Decimal_longitude,Longitude_Hemisphere)  #Affichage des Coordonées Reçu par le Stick GPS USB Série


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
