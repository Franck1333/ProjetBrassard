#!/usr/bin/env python
# -*- coding: UTF8 -*-

#Aides : https://developers.deezer.com/api 

import json         #Traitement du fichier JSON reçu
import requests     #<-- Utilisation d'une Adresse URL Normalisée

#Blibliothèque RANDOM pour l'utilisation de l'aléatoire
import random

def top_chart_suggestion():

    send_url = 'https://api.deezer.com/chart'
    r = requests.get(send_url)          #<-- Ouverture de L'URL pour l'utilisation de L'API
    jdict = json.loads(r.text)          #Chargement des données reçu dans le fichier en format JSON

    INDICE = random.randrange(1,10,1)   #Le systeme choisi au hasard entre les 10 titres présent dans le top 10 un seul morceau

    print("Information Provenant de: https://www.deezer.com/")                      #Message Console
    print("\n")                                                                     #Saut de ligne

    print("Voici ce que nous vous suggérons aujourd'hui:")                          #Message permettant de connaitre le placement d'un Artiste/Groupe dans le TOP10
    
    print("Titre du Morceau:", jdict['tracks']['data'][INDICE]['title'])            #Permet de connaitre le Titre du Morceau

    print("Album du Morceau:", jdict['tracks']['data'][INDICE]['album']['title'])   #Permet de connaitre le Nom de l'Album

    print("Nom de l'Artiste:", jdict['tracks']['data'][INDICE]['artist']['name'])   #Permet de connaitre le Nom de l'Artiste/Groupe    

    print("Lien Deezer:", jdict['tracks']['data'][INDICE]['artist']['link'])        #Affichage du Lien Deezer de l'Artiste/Groupe

    print("\n")

    Titre_Morceau = jdict['tracks']['data'][INDICE]['title']
    Album_Morceau = jdict['tracks']['data'][INDICE]['album']['title']
    Nom_Artiste =  jdict['tracks']['data'][INDICE]['artist']['name']
    Lien_Deezer = jdict['tracks']['data'][INDICE]['artist']['link']

    return Titre_Morceau,Album_Morceau,Nom_Artiste,Lien_Deezer

if __name__ == "__main__":
    top_chart_suggestion()  #Fonctionnalité permettant de suggérer a l'utilisateur un morceau provenant du TOP10 actuel.
