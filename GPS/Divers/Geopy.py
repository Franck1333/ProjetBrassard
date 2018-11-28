#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#AIDES: https://github.com/geopy/geopy
#AIDES: https://pypi.org/project/geopy/
#AIDES: https://geopy.readthedocs.io/en/stable/index.html?highlight=reverse

import geopy.geocoders                  #--> sudo pip install geopy 
from geopy.geocoders import Nominatim   #Nominatim Service

#---
#Cette blibliothèque permet de travailler avec du contenue contenant des accents
import unidecode #--> sudo pip install unicode

#unaccented_location = unidecode.unidecode(location.address)
#---

geolocator = Nominatim(user_agent="GPS-SWAGG")                          #Utilisation des Services de Reverse-Geocoding de Nominatim, https://nominatim.openstreetmap.org/reverse.php?format=html
location = geolocator.reverse("47.2224326667, -0.729606666667")         #Envoie aux Services de Nominatim les coordonées GPS et reception de la Réponse

unaccented_location = unidecode.unidecode(location.address)             #On Retire les Accents de la Réponse de l'API
print("\n")                                                             #Saut de ligne
print(unaccented_location)                                              #Affichage de la Réponse (sans accents)
print("\n")                                                             #Saut de Ligne
#Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union

print((location.latitude, location.longitude))                          #Affichage des coordonées du Lieu indiqué
#(52.5094982, 13.3765983)

print("\n")
#print(location.raw)

Ville =         location.raw['address']['town']
Numero_Maison = location.raw['address']['house_number']
Rue =           location.raw['address']['road']
Code_Postal =   location.raw['address']['postcode']
Pays =          location.raw['address']['country']

print(Ville)
print(Numero_Maison)
print(Rue)
print(Code_Postal)
print(Pays)
#{'place_id': '654513', 'osm_type': 'node', ...}
