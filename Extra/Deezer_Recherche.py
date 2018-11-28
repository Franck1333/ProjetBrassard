#!/usr/bin/env python
# -*- coding: UTF8 -*-

#Aides : https://developers.deezer.com/api
#Aides : http://json.parser.online.fr/


import json                         #Traitement du fichier JSON reçu
import requests                     #<-- Utilisation d'une Adresse URL Normalisée

from PIL import Image               #Fonctionnalité lié à la Recuperation et Affichage des Illustrations
import urllib, cStringIO            #Fonctionnalité lié à la Recuperation et Affichage des Illustrations

def recherche():
    #Procéder à une recherche de contenue sur Deezer.

    print("Bienvenue dans le Programme de Recherche de contenue disponible sur Deezer.")    #Affichage de Bienvenue
    recherche = raw_input("Que souhaitez-vous cherchez ?")                                  #Permet le Saisie du contenue rechercher en utilisant le clavier
    
    send_url = 'https://api.deezer.com/search?q='+recherche                                 #Envoie de la Demande cliente a l'API Deezer
    r = requests.get(send_url)                                                              #<-- Ouverture de L'URL pour l'utilisation de L'API
    jdict = json.loads(r.text)                                                              #Chargement des données reçu dans le fichier en format JSON

    #print(jdict)

    INDICE = 0                              #Indice permettant le Traitement des données provenant du fichier JSON
    Taille_reponse = len(jdict['data'])     #Permet de determiné la taille exacte de la Réponse reçu; Donc permet de determiné le nombre réponse obtenue

    for INDICE in range(len(jdict['data'])):                                        #Traitement à partir de 0 jusqu'a la taille de la Réponse reçu 

        print("\n")                                                                 #Saut de ligne
                
        print("Information Provenant de: https://www.deezer.com/")                  #Message Console
        print("Voici le(s) Résultats obtenue(s) pour votre recherche:  ")           #Message Console

        print("Nom de l'Artiste/Groupe:",jdict['data'][INDICE]['artist']['name'] )  #Affichage du Nom de L'Artiste/Groupe dans la console

        print("Titre du Morceau:",jdict['data'][INDICE]['title'] )                  #Affichage du Titre du Morceau

        print("Titre de l'Album:", jdict['data'][INDICE]['album']['title'])         #Affichage du Nom de L'Album

        print("Resultat Numero:",INDICE +1, "sur" ,Taille_reponse)                  #Indication où sommes nous dans la recherche tant sur tant.

        #print("\n")

        #print("Lien Illustration Artiste:", jdict['data'][INDICE]['artist']['picture_small'])
        #file = cStringIO.StringIO(urllib.urlopen(jdict['data'][INDICE]['artist']['picture_small']).read())
        #img = Image.open(file)

        #print("Lien Illustration Album:", jdict['data'][INDICE]['album']['cover_small'])
        #file = cStringIO.StringIO(urllib.urlopen(jdict['data'][INDICE]['album']['cover_small']).read())
        #img = Image.open(file)

        #print("\n")

        print("Lien Deezer:", jdict['data'][INDICE]['artist']['link'])              #Affichage du Lien Deezer de l'Artiste/Groupe correspondant

        print("\n")                                                                 #Saut de ligne

    if len(jdict['data']) == 0:                                                     #Si la recherche ne retourne aucune information, alors...
        print("\n")
        
        print("Ouille!!!! Aucun Resultat n'a ete trouver pour votre recherche!!!")  #Alors , dans ce cas on affiche un message d'erreur
        print("On recommence ???")                                                  #Message Console
        
        print("\n")                                                                 #Saut de ligne
        


if __name__ == "__main__":
    recherche()             #Fonctionnalité permettant de rechercher du contenue sur Deezer.   


    
