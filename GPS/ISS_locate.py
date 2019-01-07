#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides : http://api.open-notify.org/
#Aides : http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
#Aides : http://open-notify.org/Open-Notify-API/ISS-Location-Now/
#Aides : https://geopy.readthedocs.io
#Aides : http://json.parser.online.fr/beta/

import json         #Traitement du fichier JSON reçu
import requests     #<-- Utilisation d'une Adresse URL Normalisée
import time         #Gestion des Timestamp
import datetime     #Gestion des Convertions des Durees Secondes/Minutes
from Recuperation_Determination import lecture_return_serie     #Obtention des Coordonnee GPS actuel
from nettoyage_du_cache import clear_cache                      #Programme de Nettoyage des Fichiers cache genere par Python


def GPS_Predict_ISS():
    latitude,longitude,Validite,dir_Latitude_Hemisphere,dir_Longitude_Hemisphere, = lecture_return_serie()
    print(latitude)
    print(longitude)

    send_url = "http://api.open-notify.org/iss-pass.json?lat="+str(latitude)+"&lon="+str(longitude)+""
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    resultat = json.loads(r.text)   #Chargement des données reçu dans le fichier en format JSON

    #print(resultat)
    print("Voici les prochaines Apparitions de l'ISS a votre position: ")

    #---TRAITEMENT DES DONNEES---
    #Il y aura un FOR

    INDICE = 0                                      #Indice permettant le Traitement des données provenant du fichier JSON
    Taille_reponse = len(resultat['response'])      #Permet de determiné la taille exacte de la Réponse reçu; Donc permet de determiné le nombre réponse obtenue

    for INDICE in range(len(resultat['response'])):                                 #Traitement à partir de 0 jusqu'a la taille de la Réponse reçu 

        print("\n")                                                                 #Saut de ligne
        print("Voici l'Apparition Numero #"+ str(INDICE) + " de l'ISS a votre position: ")

        reponse_duration = resultat['response'][INDICE]['duration']                 #Reception de la Valeur correspondant au Temps d'Apparition de l'ISS dans le Ciel
        reponse_risetime = resultat['response'][INDICE]['risetime']                 #Reception de la Valeur correspondant au Moment de l'Apparition de l'ISS dans le Ciel
        
        #CONVERTION EN VARIABLE LISIBLE
        lisible_duration = str(datetime.timedelta(seconds=reponse_duration))        #On convertis les Secondes en Formats Heures:Minutes:Secondes lisibles par tous
        lisible_apparition = str(time.ctime(reponse_risetime))                      #On convertis le Format Timestamp en format habituel Humain des Dates

        print("Duree #" + str(INDICE) + ": " , lisible_duration)                    #On affiche la Duree de l'Apparition convertis dans la Console
        print("Apparition #"+ str(INDICE) + ": ", lisible_apparition)               #On Affiche la Date d'Apparition convertis dans la Console

        print("\n")                                                                 #Saut de ligne pour plus de Clarete dans la console
    #---
    #Gestion des Timestamp
    #>>> import time
    #>>> lisible = time.ctime(1544619861)
    #>>> print(lisible)
    #Wed Dec 12 14:04:21 2018
    #--
    #Gestion des Durees en Minutes/Secondes
    #>>> import datetime
    #>>> str(datetime.timedelta(seconds=666))
    #'0:11:06'
    #---    
    #---TRAITEMENT DES DONNEES---
    return INDICE,Taille_reponse,lisible_duration,lisible_apparition

def GPS_Now_ISS():
    global ISS_latitude
    global ISS_longitude

    send_url = "http://api.open-notify.org/iss-now.json"
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    resultat = json.loads(r.text)   #Chargement des données reçu dans le fichier en format JSON

    #print(resultat)

    reponse_date =          resultat['timestamp']                           #Recuperation de la Date de capture des Informations
    reponse_ISS_latitude =  resultat['iss_position']['latitude']            #Recuperation de la Latitude actuel de l'ISS
    reponse_ISS_longitude = resultat['iss_position']['longitude']           #Recuperation de la Longitude actuel de l'ISS

    lisible_apparition = str(time.ctime(reponse_date))                      #On convertis le Format Timestamp en format habituel Humain des Dates
    ISS_latitude = str(reponse_ISS_latitude)                                #On convertis la Latitude en 'string' pour une utilisation ulterieur de la Valeur
    ISS_longitude = str(reponse_ISS_longitude)                              #On convertis la Longitude en 'string' pour une utilisation ulterieur de la Valeur

    print("\n")                                                             #Saut de Ligne

    print("A cette Date soit le "+lisible_apparition+" , La Station Spaciale International ce situe au-dessus de ces coordonées GPS: ")   #Affichage de la Date recue
    tk_lisible_apparition = "A cette Date soit le "+str(lisible_apparition)+" , La Station Spaciale International ce situe au-dessus de ces coordonées GPS: "

    print("Latitude: ", ISS_latitude)                                                                                           #Affichage de la Latitude actuel de l'ISS
    tk_ISS_latitude = "Latitude: "+ str(ISS_latitude)

    print("Longitude: ", ISS_longitude)                                                                                         #Afficghage de la Longitude actuel de l'ISS
    tk_ISS_longitude= "Longitude: "+ str(ISS_longitude)
    
    Emplacement_ISS = determine_less_ISS()
    print("Elle ce trouve au-dessus de: ", Emplacement_ISS)                                                                     #Affichage de la Localisation e l'ISS par rapport a la Terre
    tk_Emplacement_ISS = "Elle ce trouve au-dessus de: "+ str(Emplacement_ISS)
    
    print("\n")                                                                                                                 #Saut de ligne
    #---
    #Gestion des Timestamp
    #>>> import time
    #>>> lisible = time.ctime(1544619861)
    #>>> print(lisible)
    #Wed Dec 12 14:04:21 2018
    #--
    return tk_lisible_apparition,tk_ISS_latitude,tk_ISS_longitude,tk_Emplacement_ISS

                            #Localisation
def determine_less_ISS():   #Cette fonctionnalité est Utilise par GPS_Now_ISS() pour Identifier le Lieu sous forme Textuel a l'aide des Coordonnees G.P.S.
    #---REVERSE_GEOCODING_GEOPY---
    import geopy.geocoders                  #--> sudo pip install geopy 
    from geopy.geocoders import Nominatim   #Nominatim Service
    #---REVERSE_GEOCODING_GEOPY---
    import unidecode

    global resultats
    global EmplacementComplet
    EmplacementComplet = "Inconnu/Unknow"
    #global Ville
    #global Pays
    #Ville= None
    #Pays = None
    
    geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html
    coordonees_GPS = ISS_latitude +","+ ISS_longitude
    #print(coordonees_GPS)
    location = geolocator.reverse(coordonees_GPS)                           #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

    try:
        ReponseIndisponible = location.raw['error']
        if ReponseIndisponible != None :                                                    #Dans le cas ou la Station est au-dessus d'une Zone non Identifiable, donc que la Valeur "ReponseIndisponible" a une definition, alors ...
            print("Localisation Indisponible, La Station doit être au-dessus des Oceans...")#On affiche un message dans la console
            print(ReponseIndisponible)                                                      #On affiche la Valeur recue de "ReponseIndisponible"
            Ville = str(ReponseIndisponible)                                                #La Valeur "Ville" sera egale a la variable d'erreur pour un affichage dans l'interface et la console
            Pays = "Impossible de Localiser l'ISS"                                          #La Valeur "Pays" sera egale a une chaine de caractere pour informer et afficher l'information dans l'interface
            resultats = Ville,Pays                                                          #Et On enregistre ces deux Variables dans une seul variable pour plus de Facilite et de clarete
            pass
    except KeyError:                                                                        #Dans le cas ou la Station ce situe au-dessus d'une Zone Identifiable et que donc le champ 'error' n'existe pas dans la reponse JSON de l'API source...
            print("\n")                                                                     #Saut a la ligne
            #print(location.raw)                                                            #Affichage du fichier JSON recue au complet
            print((location.latitude, location.longitude))                                  #Affichage des coordonées du Lieu indiqué
            #(52.5094982, 13.3765983)
            EmplacementComplet_accented = location.raw['display_name']                      #Enregistrement de l'Emplacement Complet de la Localisation
            EmplacementComplet = unidecode.unidecode(EmplacementComplet_accented)
            print(EmplacementComplet)                                                       #Affichage de l'Emplacement Complet de l'ISS
                    #try:
                    #Ville =         location.raw['address']['town']                                        #Enregistrement de la Ville depuis la version "RAW" du Service Nominatim
                    #Pays =          location.raw['address']['country']                                     #Enregistrement du Pays depuis la version "RAW" du Service Nominatim
                    #except KeyError:
                    #    if Ville == None :                                                                 #Au cas ou la Valeur "Ville" n'est pas Definie
                    #        Ville = "Inconnu/Unknow"                                                       #On indique dans une chaine de caractere que l'Information est inconnu
                    #        print(Ville)                                                                   #On affiche cette information pour le DEBUG
                    #    elif Pays == None :                                                                #Au cas ou la Valeur "Pays" n'est pas Definie
                    #        Pays = "Inconnu/Unknow"                                                        #On indique dans une chaine de caractere que l'information est Unknow 
                    #        print(Pays)                                                                    #On affiche cette information dans la Console pour DEBUG   
                    #print(Ville)                                                                           #Affichage de la Ville dans la Console
                    #print(Pays)                                                                            #Affichage du Pays dans la Console
                    #{'place_id': '654513', 'osm_type': 'node', ...}                                        #Exemple du format des données reçu enregistrer dans "location.raw"
                    #resultats = Ville,Pays                                                                 #Et On enregistre ces deux Variables dans une seul variable pour plus de Facilite et de clarete
    return EmplacementComplet #Puis pour finir on retourne cette dite variable pour une ulterieur utilisation de cette fonctionnalitee
    
def Share_Location_ISS():
        GPS_Now_ISS()
        ISS_latitude_shared = ISS_latitude
        ISS_longitude_shared = ISS_longitude
        return ISS_latitude_shared,ISS_longitude_shared

if __name__ == "__main__":
    GPS_Now_ISS()           #Obtention de la Localisation en Temp Reel de la Station Spacial International
    GPS_Predict_ISS()       #Obtentionde du Passage predit de l'ISS a la Position GPS actuel de l'utilisateur
    clear_cache()           #Nettoie les fichiers caches generer par le Language Python
    
