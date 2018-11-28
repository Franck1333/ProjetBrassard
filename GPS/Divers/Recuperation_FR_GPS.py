#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
#https://gist.github.com/Lauszus/5785023
#https://raspberry-pi.developpez.com/cours-tutoriels/projets-rpi-zero/traceur-gps/

import serial
import time
import os
import sys

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S 

#Recuparation des informations de la Trame GPRMC contenant les coordonnees GPS principales

# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
def parse_GPRMC(data):
    data = data.split(',')
    dict = {
            'Temps_Capture': data[1],
            'Validite': data[2],
            'Latitude': data[3],
            'Latitude_Hemisphere' : data[4],
            'Longitude' : data[5],
            'Longitude_Hemisphere' : data[6],
            'Vitesse': data[7],
            #'Angle': data[8],
            #'fix_date': data[9],
            #'variation': data[10],
            #'variation_e_w' : data[11],
            'Checksum' : data[12]
    }

    return dict

def envoie():

    print (gpsData) #Affiche les données GPS
    return gpsData  #Retourne les données GPS pour une utilisation ultérieur

while True:

    line = ser.readline() #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line: #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line) #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'

        envoie(); #Utilisation de la fonction envoie()
