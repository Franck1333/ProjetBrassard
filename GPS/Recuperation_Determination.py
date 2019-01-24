#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
#https://gist.github.com/Lauszus/5785023
#https://raspberry-pi.developpez.com/cours-tutoriels/projets-rpi-zero/traceur-gps/
#https://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city
#AIDES: https://github.com/geopy/geopy
#AIDES: https://pypi.org/project/geopy/
#AIDES: https://geopy.readthedocs.io/en/stable/index.html?highlight=reverse

import serial
import time
import os
import sys
from urllib2 import urlopen
#from urllib.request import urlopen
import json

#---REVERSE_GEOCODING_GEOPY---
import geopy.geocoders                  #--> sudo pip install geopy 
from geopy.geocoders import Nominatim   #Nominatim Service
#---REVERSE_GEOCODING_GEOPY---

#---
#Cette blibliothèque permet de travailler avec du contenue contenant des accents
import unidecode #--> sudo pip install unidecode
#unaccented_location = unidecode.unidecode(valeur)
#---

import datetime

from nettoyage_du_cache import clear_cache

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

#---DEBUT---Variables Par Défault---
Validite = None
Decimal_latitude = None
Decimal_longitude = None
#---FIN---Variables Par Défault---

ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S

#Recuparation des informations de la Trame GPRMC contenant les coordonnees GPS principales
# Helper function to take HHMM.SS, Hemisphere and make it decimal:
#-------------------------------
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""
#-------------------------------    
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
    dict['decimal_latitude'] = degrees_to_decimal(dict['Latitude'], dict['Latitude_Hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['Longitude'], dict['Longitude_Hemisphere'])

    global Validite
    global Latitude
    global Longitude

    global Latitude_Hemisphere
    global Longitude_Hemisphere

    global Decimal_latitude    #VARIABLE GLOBAL CONVERTIS LATITUDE
    global Decimal_longitude   #VARIABLE GLOBAL CONVERTIS LONGITUDE

    Validite = dict['Validite']
    Latitude = dict['Latitude']
    Longitude = dict['Longitude']

    Latitude_Hemisphere = dict['Latitude_Hemisphere']
    Longitude_Hemisphere = dict['Longitude_Hemisphere']    
    
    Decimal_latitude = dict['decimal_latitude']   #DICTIONNAIRE VARIABLE LATITUDE CONVERTIS
    Decimal_longitude = dict['decimal_longitude'] #DICTIONNAIRE VARIABLE LONGITUDE CONVERTIS

    #print("La Direction du CAP:",Decimal_latitude,Latitude_Hemisphere,'-',Decimal_longitude,Longitude_Hemisphere ) #TEST - DEBUG
      
    return Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere #RETOURNE LES VARIABLES CONVERTIS LATITUDE,LONGITUDE
    
   #return dict #Retourne le dictionnaire principale
#-------------------------------

#-------------------------------
def etat_trame(): #Verification de la conformite de la Trame NMEA reçu

    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    #print (system_time)
    #-- FIN -- Heure,Minute,Seconde

    #Zone de TEST --DEBUT--
    #Permet de Savoir si l'information est de type correcte par rapport au type indiqué dans les paramètres de issinstance(), réponse booléenne.
    #Validite_valid = isinstance(Validite,str) #<-- TEST
    Decimal_latitude_valid = isinstance(Decimal_latitude,float) #<-- TEST
    Decimal_longitude_valid = isinstance(Decimal_longitude,float) #<-- TEST
    #Zone de TEST --FIN--


    #Cette fonction va verifie la conformite de la Trame NMEA reçu par le Stick GPS et relance le Menu Principal si une erreur est detecte en testant la variable 'Validite'
    if Validite == 'A' and Decimal_latitude_valid == True and Decimal_longitude_valid == True :   #Si la variable est valide alors...
        
        print(Validite)                 #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA Valide")      #Affichage du String entre guillemet
        print("Signal GPS Obtenue")     #Affichage du String entre guillemet
        print (system_time)
        pass #<--   
    

    elif Validite == None or Decimal_latitude == None or Decimal_longitude == None  : #Sinon alors...

        print("elif Variables == None")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)
    
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

        exit

    elif Decimal_latitude_valid == False : #Sinon alors...

        print("elif Decimal_latitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)
        
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--
        exit
        
    elif Decimal_longitude_valid == False  : #Sinon alors...

        print("elif Decimal_longitude_valid == False ")
        print("Variables Non Utilisable")                           #Affichage du String entre guillemet
        print("Signal GPS Perdue")                                  #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)
        
        time.sleep(5)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--

        exit 
    else :                                                  #Sinon alors...
        
        print("else conditions")
        print(Validite)                                     #Affichage de la Variable "Validite" dans la console
        print("Trame NMEA NON VALIDE")                      #Affichage du String entre guillemet
        print("Signal GPS Perdue")                          #Affichage du String entre guillemet
        print("Redemarrage en cours du Programme MENU PRINCIPAL")
        print (system_time)
        
        time.sleep(13)
        clear_cache()                       #Nettoyage des Fichiers caches PYTHON
        #os.system('sudo python /home/pi/GPS_Display/Mon_Travail/dot3k_automenu.py') #Redemarre le Menu et les fonctions dans le Menu avec <--
        exit

#-------------------------------

#-------------------------------
def retourne_latitude():
    
    Retourne_latitude = Decimal_latitude #Initialisation de la nouvelle variable à la Latitude pour le partage avec un autre fichier python
    
    return Retourne_latitude #Retourne la nouvelle Valeur LATITUDE   
#-------------------------------
#-------------------------------
def retourne_longitude():
        
    Retourne_longitude = Decimal_longitude #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_longitude #Retourne la nouvelle Valeur LONGITUDE
#-------------------------------
#-------------------------------
def retourne_Latitude_Hemisphere():

    Retourne_Latitude_Hemisphere = Latitude_Hemisphere      #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_Latitude_Hemisphere                     #Retourne la nouvelle Valeur LATITUDE_HEMISPHERE

#-------------------------------
#-------------------------------
def retourne_Longitude_Hemisphere():

    Retourne_Longitude_Hemisphere = Longitude_Hemisphere    #Initialisation de la nouvelle variable à la Longitude pour le partage avec un autre fichier python

    return Retourne_Longitude_Hemisphere                    #Retourne la nouvelle Valeur LONGITUDE_HEMISPHERE
#-------------------------------
def determine():
    etat_trame() #Validation de la conformite de la Trame NMEA <--

    
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html

    coordonees_GPS = str(Decimal_latitude) +","+ str(Decimal_longitude)

    print(coordonees_GPS)

    location = geolocator.reverse(coordonees_GPS)      #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
    print("\n")                                                             #Saut de ligne
    print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
    print("\n")                                                             #Saut de Ligne
    #Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

    print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
    #(52.5094982, 13.3765983)

    print("\n")
    #print(location.raw)

    Ville =         location.raw['address']['town']                         #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
    Numero_Maison = location.raw['address']['house_number']                 #Enregistrement du Numéro de Rue depuis la version "RAW" du Service Nominatim
    Rue =           location.raw['address']['road']                         #Enregistrement de la Rue depuis la version "RAW" du Service Nominatim
    Code_Postal =   location.raw['address']['postcode']                     #Enregistrement du Code Postal depuis la version "RAW" du Service Nominatim
    Pays =          location.raw['address']['country']                      #Enregistrement du Pays depuis la version "RAW" du Service Nominatim

    print(Ville)                                                            #Affichage de la Ville
    print(Numero_Maison)                                                    #Affichage du Numéro de Positionnement dans la Rue
    print(Rue)                                                              #Affichage du Nom de la Rue
    print(Code_Postal)                                                      #Affichage du Code Postal
    print(Pays)                                                             #Affichage du Pays
    #{'place_id': '654513', 'osm_type': 'node', ...}                        #Exemple du format des données reçu enregistrer dans "location.raw"
    resultat_Ville = Ville
    return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE    
#-------------------------------

#-------------------------------
def determine_Brassard():
    etat_trame() #Validation de la conformite de la Trame NMEA <--
    
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html

    coordonees_GPS = str(Decimal_latitude) +","+ str(Decimal_longitude)

    #print(coordonees_GPS)

    location = geolocator.reverse(coordonees_GPS,timeout=73)      #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    #unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
    #print("\n")                                                             #Saut de ligne
    #print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
    #print("\n")                                                             #Saut de Ligne
    #Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

    #print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
    #(52.5094982, 13.3765983)

    #print("\n")
    #print(location.raw)

    Ville =         location.raw['address']['town']                         #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
    Numero_Maison = location.raw['address']['house_number']                 #Enregistrement du Numéro de Rue depuis la version "RAW" du Service Nominatim
    Rue =           location.raw['address']['road']                         #Enregistrement de la Rue depuis la version "RAW" du Service Nominatim
    Code_Postal =   location.raw['address']['postcode']                     #Enregistrement du Code Postal depuis la version "RAW" du Service Nominatim
    Pays =          location.raw['address']['country']                      #Enregistrement du Pays depuis la version "RAW" du Service Nominatim

    #print(Ville)                                                            #Affichage de la Ville
    #print(Numero_Maison)                                                    #Affichage du Numéro de Positionnement dans la Rue
    #print(Rue)                                                              #Affichage du Nom de la Rue
    #print(Code_Postal)                                                      #Affichage du Code Postal
    #print(Pays)                                                             #Affichage du Pays
    #{'place_id': '654513', 'osm_type': 'node', ...}                        #Exemple du format des données reçu enregistrer dans "location.raw"

    #if Ville or Numero_Maison or Rue or Code_Postal or Pays == None :
    #    Ville = "Problème Service"
    #    Numero_Maison = 0
    #    Rue = "Problème Service"
    #    Code_Postal = 0000
    #    Pays = "Code Erreur = Variables Non Définies"

    return Ville,Numero_Maison,Rue,Code_Postal,Pays
#-------------------------------


#-------------------------------
#NOUS INDICONS UNIQUEMENT LA VILLE ICI
def determine_less():
    etat_trame() #Validation de la conformite de la Trame NMEA <--
    
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html

    coordonees_GPS = str(Decimal_latitude) +","+ str(Decimal_longitude)

    print(coordonees_GPS)

    location = geolocator.reverse(coordonees_GPS)      #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
    print("\n")                                                             #Saut de ligne
    print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
    print("\n")                                                             #Saut de Ligne
    #Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

    print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
    #(52.5094982, 13.3765983)

    print("\n")
    #print(location.raw)

    Ville =         location.raw['address']['town']                         #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
    Pays =          location.raw['address']['country']                      #Enregistrement du Pays depuis la version "RAW" du Service Nominatim

    print(Ville)                                                            #Affichage de la Ville
    print(Pays)                                                             #Affichage du Pays
    #{'place_id': '654513', 'osm_type': 'node', ...}                        #Exemple du format des données reçu enregistrer dans "location.raw"
    resultat_Ville = Ville
    return resultat_Ville #RETOURNE LE STRING DE LA LOCALISATION DETERMINE
#-------------------------------#NOUS INDICONS UNIQUEMENT LA VILLE ICI
#-------------------------------
#-------------------------------
def lecture_serie():
    line = ser.readline()                   #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line:                    #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line)         #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------
#-------------------------------
def lecture_return_serie():
    global gpsData
    gpsData = None
    while gpsData == None :                                 #Tant que 'gpsData' est non définie alors on capture les information provenant du port serie et on retourne le resultat.

        ser = serial.Serial('/dev/ttyACM0',4800,timeout=0)  #Open Serial port Configure le Recepteur G.P.S

        data = ser.readline()                               #Lecture de la liason serie Ligne par Ligne
    
        if "$GPRMC" in data:                                #SELECTION DE LA LIGNE GPRMC  
             gpsData = parse_GPRMC(data)                    #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
             
    return gpsData
#-------------------------------
#-------------------------------
def ouverture_serie():
    ser = serial.Serial('/dev/ttyACM0',4800,timeout=1) # Open Serial port Configure le Recepteur G.P.S
    return ser
        
#-------------------------------
def meteo():
    line = ser.readline()                   #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line:                    #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line)         #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------
def recup_affichage():
    line = ser.readline()                   #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line:                    #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line)         #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
    #etat_trame()
#-------------------------------        

#---MAIN---
def main():
    line = ser.readline()                   #Lecture de la liason serie Ligne par Ligne

    if "$GPRMC" in line:                    #SELECTION DE LA LIGNE GPRMC
        gpsData = parse_GPRMC(line)         #ENREGISTREMENT DES DONNEES GPS DANS LA VARIABLE Globale 'gpsData'
        
        print(Decimal_latitude)             #AFFICHAGE DE LA VARIABLE CONVERTIS LATITUDE
        print(Decimal_longitude)            #AFFICHAGE DE LA VARIABLE CONVERTIS LONGITUDE
        etat_trame()                        #Validation de la conformite de la Trame NMEA <--
        determine();                        #FONCTION PERMETTANT DE DETERMINER LA LOCALISATION GRACE AU G.P.S
        #determine_less()
        
if __name__ == "__main__":
    try:                                                                #---!!!GESTION DES ERREURS!!!---
        main()
        clear_cache()
        pass
    except TypeError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console                              
	print("Code Erreur: TypeError")
        clear_cache()
    except ValueError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: ValueError")
        clear_cache()
    except AssertionError:
	print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: AssertionError")
        clear_cache()
    except NameError:
	print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: NameError")
        clear_cache()
    except KeyError:
	print("Une API à eu un problème d'enregistrement de Valeur, Il est necessaire de Redemarrez le GPS!")                    #On affiche ce message dans la console
        print("Code Erreur: KeyError")
        clear_cache()
    
    except:
	print("Il est necessaire de Redemarrez le GPS!")                                #On affiche ce message dans la console
        print("Code Erreur: Aucun")
        clear_cache()
                                                                         #---!!!GESTION DES ERREURS!!!---
