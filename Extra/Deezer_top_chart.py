#!/usr/bin/env python
# -*- coding: UTF8 -*-

#Aides : https://developers.deezer.com/api 

import json         #Traitement du fichier JSON reçu
import requests     #<-- Utilisation d'une Adresse URL Normalisée

def top_chart():

    send_url = 'https://api.deezer.com/chart'
    r = requests.get(send_url)      #<-- Ouverture de L'URL pour l'utilisation de L'API
    jdict = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    #print(j)

    #print("Titre du Morceau:", jdict['tracks']['data'][0]['title'])

    #print("Album du Morceau:", jdict['tracks']['data'][0]['album']['title'])

    #print("Nom de l'Artiste:", jdict['tracks']['data'][0]['artist']['name'])

    #print("Placement TOP10:", jdict['tracks']['data'][0]['position'])

    #print("Lien Deezer:", jdict['tracks']['data'][0]['artist']['link'])


    INDICE_TOP10 = 0                                                                          #Indice permettant le Traitement des données provenant du fichier JSON

    TailleFOR_TOP10 = len(jdict['tracks']['data'])

    for INDICE_TOP10 in range(TailleFOR_TOP10):                                  #Traitement à partir de 0 jusqu'a la taille de la Réponse reçu 

        print("\n")                                                                     #Saut de ligne

        print("Information Provenant de: https://www.deezer.com/")                      #Message Console
        print("Placement TOP10:", jdict['tracks']['data'][INDICE_TOP10]['position'])          #Message permettant de connaitre le placement d'un Artiste/Groupe dans le TOP10
        
        print("Titre du Morceau:", jdict['tracks']['data'][INDICE_TOP10]['title'])            #Permet de connaitre le Titre du Morceau

        print("Album du Morceau:", jdict['tracks']['data'][INDICE_TOP10]['album']['title'])   #Permet de connaitre le Nom de l'Album

        print("Nom de l'Artiste:", jdict['tracks']['data'][INDICE_TOP10]['artist']['name'])   #Permet de connaitre le Nom de l'Artiste/Groupe    

        print("Lien Deezer:", jdict['tracks']['data'][INDICE_TOP10]['artist']['link'])        #Affichage du Lien Deezer de l'Artiste/Groupe

        print("\n")                                                                     #Saut à la ligne

    

    return jdict,INDICE_TOP10,jdict['tracks']['data'][INDICE_TOP10]['position'],jdict['tracks']['data'][INDICE_TOP10]['title'],jdict['tracks']['data'][INDICE_TOP10]['album']['title'],jdict['tracks']['data'][INDICE_TOP10]['artist']['name'],jdict['tracks']['data'][INDICE_TOP10]['artist']['link'],TailleFOR_TOP10 

if __name__ == "__main__":
    top_chart()             #Fonctionnalité permettant de connaitre le TOP10 actuel.   
