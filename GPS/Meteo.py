#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
#https://github.com/csparpa/pyowm #pip install pyowm
#http://pyowm.readthedocs.io/en/latest/index.html

import serial
import time
import os
import sys

from Recuperation_Determination import retourne_latitude
from Recuperation_Determination import retourne_longitude
from Recuperation_Determination import meteo

from nettoyage_du_cache import clear_cache

import pyowm

def main_meteo():
    
    owm = pyowm.OWM('7435ea1b7ee5e31fe1f524a922202510',language = "en")
    # You MUST provide a valid API key
    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
    # Search for current weather in London (Great Britain)
    #observation = owm.weather_at_place('London,GB')
    #w = observation.get_weather()
    #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                  # status=Clouds>
    # Weather details
    #w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    #w.get_humidity()              # 87
    #w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    #print (w.get_temperature('celsius'))
    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)

    #----------------------------------------------------------------------------------------------------------------------------
    meteo() #MAIN DU FICHIER Recuperation_Determination.py permettant de lancer la capture des infomations provenant du STICK GPS
    #observation = owm.weather_at_coords(47.066316799999996,-0.6365184)   #CIBLE TEST
    print(retourne_latitude())
    print(retourne_longitude())
    observation = owm.weather_at_coords(retourne_latitude(),retourne_longitude())   #Recuperation des Coordonnees du lieu cible
    z = observation.get_weather()                           #Obtention des donnees meteorologique via les coordonees

    global vitesse_du_vent
    global status_climat
    global volume_de_neige
    global volume_de_pluie
    global couverture_de_nuage
    global pourcentage_humidite
    global lever_du_soleil
    global coucher_du_soleil

    vitesse_du_vent = z.get_wind()['speed']         # Get wind speed
    status_climat = z.get_detailed_status()         # Get detailed weather status
    volume_de_neige = z.get_snow()                  # Get snow volume
    volume_de_pluie = z.get_rain()                  # Get rain volume
    couverture_de_nuage = z.get_clouds()            # Get cloud coverage
    pourcentage_humidite = z.get_humidity()         # Get humidity percentage
    lever_du_soleil = z.get_sunrise_time('iso')     # Sunrise time (GMT UNIXtime or ISO 8601)
    coucher_du_soleil = z.get_sunset_time('iso')    # Sunset time (GMT UNIXtime or ISO 8601)

    print("Vitesse du Vent:", vitesse_du_vent)                  #Affichages des informations voulus
    print("Conditions Meteo:",status_climat)                    #Affichages des informations voulus
    print("Volume de Neige:",volume_de_neige)                   #Affichages des informations voulus
    print("Volume de Pluie;", volume_de_pluie)                  #Affichages des informations voulus
    print("Taux de Nuage dans le ciel:",couverture_de_nuage)    #Affichages des informations voulus
    print("Taux d'Humidite:", pourcentage_humidite)             #Affichages des informations voulus
    print("Lever du Soleil:",lever_du_soleil)                   #Affichages des informations voulus
    print("Coucher du Soleil:",coucher_du_soleil)               #Affichages des informations voulus
    
    
    #print(z)                                               #Affichage du Status de l'état de la Meteo et du reference temporelle                      
    #print(z.get_temperature('celsius'))                    #Enregistrement des variables de température dans un objet
    climat_min = z.get_temperature('celsius')['temp_min']   #Stockage de la temperature Minimum d'Aujourd'hui dans une variable 
    climat_max = z.get_temperature('celsius')['temp_max']   #Stockage de la temperature Maximum d'Aujourd'hui dans une variable 
    climat_now = z.get_temperature('celsius')['temp']       #Stockage de la temperature actuel dans une variable 
    print("La Temperature MINIMAL TODAY est de:",climat_min)        #Affichages des informations voulus
    print("La Temperature MAXIMAL TODAY est de:",climat_max)        #Affichages des informations voulus
    print("La Temperature actuel est de:",climat_now)               #Affichages des informations voulus

    tk_climat_min = "La Temperature Minimal attendue aujourd'hui est de : " + str(climat_min) + " °C"
    tk_climat_max = "La Temperature Maximal attendue aujourd'hui est de : " + str(climat_max) + " °C"
    tk_climat_now= "La Temperature Actuel est de : " + str(climat_now) + " °C"
    tk_vitesse_du_vent= "La Vitesse du Vent : " + str(vitesse_du_vent) + " m/s"
    tk_status_climat = "En bref, le climat est : " + str(status_climat)
    tk_volume_de_neige = "Le volume de Neige est : " + str(volume_de_neige) 
    tk_volume_de_pluie= "Le volume de Pluie est : " + str(volume_de_pluie) 
    tk_couverture_de_nuage = "Le Taux de Nuage dans le ciel : " + str(couverture_de_nuage) + " %"
    tk_pourcentage_humidite = "Le Taux d'humidite : " + str(pourcentage_humidite) + " %"
    
    
    return tk_status_climat,tk_climat_min,tk_climat_now,tk_climat_max,tk_vitesse_du_vent,tk_volume_de_neige,tk_volume_de_pluie,tk_pourcentage_humidite,tk_couverture_de_nuage             #Retourne les valeurs obtenues
    #----------------------------------------------------------------------------------------------------------------------------

    #Il existe plusieurs façons de retourner une ou plusieurs valeurs en particuliers en python ,
    #soit en utilisant les TUPLES(ce qui est plus facile) ou en utilisant des fonctions faite uniquement dans le but de retourner une valeur en particulier,
    #mais a chaque fois que une fonction comme celle-ci est utiliser par un autre fichier python ,
    #ce fichier-ci soit re-demander une nouvelle execution d'une nouvelle capture d'information ,
    #ce que l'on doit éviter pour ne pas encombrer le réseau et ne pas être hors-forfait d'Appel API.

    #----------------------------------------------------------------------------------------------------------------------------
def Vitesse_du_vent():
    retourne_vitesse_du_vent = vitesse_du_vent
    return retourne_vitesse_du_vent
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Status_climat():
    retourne_status_climat = status_climat
    return retourne_status_climat
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Volume_de_neige():
    retourne_volume_de_neige = volume_de_neige
    return retourne_volume_de_neige
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Volume_de_pluie():
    retourne_volume_de_pluie = volume_de_pluie
    return retourne_volume_de_pluie
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Couverture_de_nuage():
    retourne_couverture_de_nuage = couverture_de_nuage
    return retourne_couverture_de_nuage
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Pourcentage_humidite():
    retourne_pourcentage_humidite = pourcentage_humidite
    return retourne_pourcentage_humidite
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Lever_du_soleil():
    retourne_lever_du_soleil = lever_du_soleil
    return retourne_lever_du_soleil
    #----------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------------------------------------
def Coucher_du_soleil():
    retourne_coucher_du_soleil = coucher_du_soleil
    return retourne_coucher_du_soleil
    #----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    clear_cache()                           #Nettoyage des Fichiers caches PYTHON
    #-----------------------------------
    try:                                                                #---!!!GESTION DES ERREURS (Simplifié)!!!---
        main_meteo()                        #Lancement du Programme Principal Météo
        pass
    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")                                                 #Affichage Code Erreur Correspondant
    except AssertionError:                                                              #Si il y a eu une erreur de TYPE de variables alors...
        print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: AssertionError")                                            #Code Erreur Correspondant
                                                                        #---!!!GESTION DES ERREURS (Simplifié)!!!---
    #-----------------------------------
