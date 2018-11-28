#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides: https://stackoverflow.com/questions/24906833/get-your-location-through-python
#Aides: https://github.com/Franck1333/GPS-Display/blob/master/Mon_Travail/Recuperation_Determination.py

import requests     #<-- Utilisation d'une Adresse URL Normalisée
import json         #<-- Permet l'expoitation de fichier en format JSON

#---REVERSE_GEOCODING_GEOPY---
import geopy.geocoders                  #--> sudo pip install geopy 
from geopy.geocoders import Nominatim   #Nominatim Service
#---REVERSE_GEOCODING_GEOPY---

import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

#---
#Cette blibliothèque permet de travailler avec du contenue contenant des accents
import unidecode #--> sudo pip install unidecode

#unaccented_location = unidecode.unidecode(valeur)
#---

from nettoyage_du_cache import clear_cache

#EXPLICATION --DEBUT--
#Ce Programme est utile pour determine la localisation de l'Adresse IP de l'utilisateur
#En revanche , ce programme n'indique pas la localisation exacte de l'utilisateur, dans ce cas elle sera imprécise!!!
#EXPLICATION --FIN--


#----------
#API https://ipstack.com

def recuperation_coordonees_ip():

    send_url = 'http://api.ipstack.com/check?access_key=b0e724b68c170a901019d01552425f1a&format=1'
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    global latitude                 #Declaration de la variable Globale 'latitude'
    global longitude                #Declaration de la variable Globale 'longitude'

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    latitude = j['latitude']        #Enregistrement de la valeur latitude du fichier JSON dans la Variable Global correspondant
    longitude = j['longitude']      #Enregistrement de la valeur longitude du fichier JSON dans la Variable Global correspondant

    city = j['city']
    region_name = j['region_name']
    ZIP = j['zip']
    country_name = j['country_name']

    global continent_name
    continent_name = j['continent_name']
    
    print(latitude)                 #Affichage de la Variable 'latitude'
    print(longitude)                #Affichage de la Variable 'longitude'
    print(continent_name)
    print("L'adresse IP a ete localiser ici:",city)
    print("Les Coordonees exactes de l'Adresse IP utilise:",continent_name,country_name,region_name,ZIP,city)
    #Information Géographique --FIN--

    return continent_name,latitude,longitude     #Retourne le nom du continent où est localiser l'adresse I.P
    #return latitude,longitude                         #Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
#----------

def recuperation_coordonees_ip_brassard():

    send_url = 'http://api.ipstack.com/check?access_key=b0e724b68c170a901019d01552425f1a&format=1'
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    global latitude                 #Declaration de la variable Globale 'latitude'
    global longitude                #Declaration de la variable Globale 'longitude'

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    latitude = j['latitude']        #Enregistrement de la valeur latitude du fichier JSON dans la Variable Global correspondant
    longitude = j['longitude']      #Enregistrement de la valeur longitude du fichier JSON dans la Variable Global correspondant

    city = j['city']
    region_name = j['region_name']
    ZIP = j['zip']
    country_name = j['country_name']

    global continent_name
    continent_name = j['continent_name']
    
    print(latitude)                 #Affichage de la Variable 'latitude'
    print(longitude)                #Affichage de la Variable 'longitude'
    print(continent_name)
    print("L'adresse IP a ete localiser ici:",city)
    print("Les Coordonees exactes de l'Adresse IP utilise:",continent_name,country_name,region_name,ZIP,city)
    #Information Géographique --FIN--

    tkk_ip              ="Votre Adresse IP Publique: " + str(ip)
    tkk_latitude        ="Latitude IP: " + str(latitude)
    tkk_longitude       ="Longitude IP: " + str(longitude)
    tkk_city            ="Ville IP: " + str(city)
    tkk_region_name     ="Région IP: "+ str(region_name)
    tkk_ZIP             ="Code Postal IP: " + str(ZIP)
    tkk_country_name    ="Pays IP: " + str(country_name)
    tkk_continent_name  ="Continent IP: " + str(continent_name)

    return tkk_ip,tkk_latitude,tkk_longitude,tkk_city,tkk_region_name,tkk_ZIP,tkk_country_name,tkk_continent_name   #Retourne toute de les information de l'adresse I.P
    #return latitude,longitude                         #Retourne les variables obtenue dans le cadre d'une utilisation ultérieur de ses valeurs
#----------

#INFORMATION :
#La localisation de exacte de l'adresse IP peut être obtenue via l'API /api.ipstack.com/ ou alors en donnant les deux valeurs latitude et longitude à une autre
#A.P.I tel que GeoPy, qui lui peut obtenir des résultats différents ou plus précis que la première API ; A vous de choisir.

#----------
#Un autre Service de GeoLocalisation de l'adresse I.P de l'utilisateur
#https://ipinfo.io/json
#Attention, ce service a une facon de Geolocaliser moins precise que le premier service juste au-dessus mais il permet d'obtenir plus d'informations sur le Fournisseur d'Acces a Internet.
#Petit détail qu'il est bon a prendre en compte.

def recuperation_coordonees_ip_brassard_V2():
    
    send_url = 'https://ipinfo.io/json'
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    global ip
    global hostname
    global org
    global loc
    global city    
    global region
    global country

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)

    hostname_accentue = j["hostname"]    #Nom de Domaine Fournisseur d'acces a Internet
    hostname = unidecode.unidecode(hostname_accentue)
    
    org_accentue = j["org"]              #Nom du F.A.I
    org = unidecode.unidecode(org_accentue)
    
    print("Nom de Domaine de l'adresse: ", hostname)
    print("Nom de l'Entreprise F.A.I :", org)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    loc = j['loc']        #Enregistrement de la valeur latitude/longitude du fichier JSON dans la Variable Global correspondant

    city_accentue = j['city']
    city = unidecode.unidecode(city_accentue)
    
    region_accentue = j['region']
    region = unidecode.unidecode(region_accentue)
    
    country_accentue = j['country']
    country = unidecode.unidecode(country_accentue)
    
    #global  continent_name
    #continent_name = j['continent_name']
    
    print("Les coordonees Physique de l'adresse: ",loc) 
    #print(continent_name)
    print("L'adresse IP a ete localiser ici:",city)
    print("Les Coordonees exactes de l'Adresse IP utilise:",country,region,city)
    #Information Géographique --FIN--

    tkk_ip              ="Votre Adresse IP Publique: " + str(ip)
    tkk_hostname        ="Nom de Domaine de l'adresse: " + str(hostname)
    tkk_org             ="Nom de l'Entreprise F.A.I: " + str(org)
    tkk_loc             ="Adresse Physique IP: " + str(loc)
    tkk_city            ="Ville IP: " + str(city)
    tkk_region          ="Région IP: "+ str(region)
    #tkk_ZIP            ="Code Postal IP: " + str(ZIP)
    tkk_country         ="Pays IP: " + str(country)
    #tkk_continent_name ="Continent IP: " + str(continent_name)

    return tkk_ip,tkk_hostname,tkk_org,tkk_loc,tkk_city,tkk_region,tkk_country  #Retourne toute de les information de l'adresse I.P
#----------


#----------
#API GeoPy

def determination():
   
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
#----------

if __name__ == "__main__":
    clear_cache()
    recuperation_coordonees_ip()                #Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur.
    #determination()                            #Fonctionnalité permettant de determiné la localisation de l'utilisateur avec son adresse I.P avec Geopy.
    recuperation_coordonees_ip_brassard_V2()    #Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur , PROVENANT d'un autre service.
    
