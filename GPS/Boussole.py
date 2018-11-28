#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :

import serial
import time
import os
import sys

from Recuperation_Determination import lecture_serie
from Recuperation_Determination import retourne_latitude
from Recuperation_Determination import retourne_longitude
from Recuperation_Determination import retourne_Latitude_Hemisphere
from Recuperation_Determination import retourne_Longitude_Hemisphere

from Recuperation_Determination import *
from Recuperation_Determination import parse_GPRMC
#from Recuperation_Determination import ouverture_serie
from Recuperation_Determination import lecture_return_serie


from nettoyage_du_cache import clear_cache

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

def boussole():
    round_retourne_latitude,round_retourne_longitude,Validite,dir_Latitude_Hemisphere,dir_Longitude_Hemisphere, = lecture_return_serie()

    #lecture_serie()                                                 #Lecture/capture des informations provenant de la liason série

    #round_retourne_latitude = retourne_latitude()                   #Enregistrement de la latitude dans une nouvelle variable
    #round_retourne_longitude = retourne_longitude()                 #Enregistrement de la longitude dans une nouvelle variable
    
    #dir_Latitude_Hemisphere = retourne_Latitude_Hemisphere()        #Enregistrement de l'information de direction hemispherique de la LATITUDE dans une nouvelle variable
    #dir_Longitude_Hemisphere = retourne_Longitude_Hemisphere()      #Enregistrement de l'information de direction hemispherique de la LONGITUDE dans une nouvelle variable

    #Zone de TEST --DEBUT--
    #Permet de Savoir si l'information est de type correcte par rapport au type indiqué dans les paramètres de issinstance(), réponse booléenne.
    #Validite_valid = isinstance(Validite,str) #<-- TEST
    round_retourne_latitude_valid = isinstance(round_retourne_latitude,float) #<-- TEST
    round_retourne_longitude_valid = isinstance(round_retourne_longitude,float) #<-- TEST
    dir_Latitude_Hemisphere_valid = isinstance(dir_Latitude_Hemisphere,str) #<-- TEST
    dir_Longitude_Hemisphere_valid = isinstance(dir_Longitude_Hemisphere,str) #<-- TEST
    #Zone de TEST --FIN--


    if round_retourne_latitude_valid and round_retourne_longitude_valid and dir_Latitude_Hemisphere_valid and dir_Longitude_Hemisphere_valid == True:   #Si les valeurs sont vérifiés et sont égale à True alors: 

        round_retourne_latitude = round(round_retourne_latitude,4)      #On selectionne que 4 chiffres après la virgule pour la latitude 
        round_retourne_longitude = round(round_retourne_longitude,4)    #On selectionne que 4 chiffres après la virgule pour la longitude

        print("La position actuel:",round_retourne_latitude,dir_Latitude_Hemisphere,'-',round_retourne_longitude,dir_Longitude_Hemisphere) #On Procède à l'affichage de toute les informations reçue

        #print(retourne_Latitude_Hemisphere())  #TEST - DEBUG
        #print(retourne_Longitude_Hemisphere()) #TEST - DEBUG


    else:                                                               #Sinon les valeurs sont mises à Zéros (pour l'affichage)
        print("Mauvaise Réception du Signal")

        round_retourne_latitude = 0                                     #0
        round_retourne_longitude = 0                                    #0
                                                                        #Sinon on affiches des messages d'erreurs dans l'interface pour informer l'utilisateur
        dir_Latitude_Hemisphere = "Mauvaise Reception GPS"              #Mauvaise Reception GPS
        dir_Longitude_Hemisphere = "Aucun Signal GPS"                   #Aucun Signal GPS

    return round_retourne_latitude,dir_Latitude_Hemisphere,round_retourne_longitude,dir_Longitude_Hemisphere    #Retourne toutes les valeurs obtenues

if __name__ == "__main__":
    clear_cache()   #Nettoyage des fichiers python indésirables
    #-----------------------------------
    try:                                                                #---!!!GESTION DES ERREURS (Simplifié)!!!---
        boussole()                                                                      #Programme principal de la Boussole Numérique (TEXTUELLE)
        pass                                                                            #On continue...
    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")                                                 #Affichage Code Erreur Correspondant
    except NameError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: NameError")                                                 #Affichage Code Erreur Correspondant   
        
                                                                        #---!!!GESTION DES ERREURS (Simplifié)!!!---
    #-----------------------------------
