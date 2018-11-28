#!/usr/bin/env python
# -*- coding: UTF8 -*-

#Aides : https://market.mashape.com/community/food2fork
#Aides : http://unirest.io/python.html
#Aides : http://json.parser.online.fr/

import requests     #<-- Utilisation d'une Adresse URL Normalisée
import json         #<-- Permet l'expoitation de fichier en format JSON

#Blibliothèque RANDOM pour l'utilisation de l'aléatoire
import random

#C'est une façon plus orienté objet pour obtenir des Réponses en format JSON , on utilise la blibliothèque "unirest".
import unirest #pip install unirest

def get_recette(): 

    #-----------------------------------------------------------
    rId = random.randrange(1,50013,1) #Cette méthode random permet de selectionner une recette parmis 50 013 recettes avec un pas de 1.
    #print(rId)

    #Par une méthode get , on effectue la requête , et on ajoute un champs headers contenant une clée "X-Mashape-Key" et le code MIME
    #J'ai utilisé ce site internet pour mieux comprendre: https://market.mashape.com/community/food2fork
    #These code snippets use an open-source library. http://unirest.io/python.html
    response = unirest.get("https://community-food2fork.p.mashape.com/get?key=a3d4e1884f608b76969149392aee7af2&rId="+str(rId),headers={"X-Mashape-Key": "J5tQc5NAVqmshY2mO24dXgZVpFv2p1zYOtNjsnuDaREl4ksB1s","Accept": "application/json"})

    #print(response.raw_body) #Affichage du Fichier JSON reçu
    j = json.loads(response.raw_body)
    #-----------------------------------------------------------

    #-----------------------------------------------------------
    Titre_recette = j['recipe']['title']                            #Enregistrement du Titre de la Recette
    auteur_recette = j['recipe']['publisher']                       #Enregistrement de l'Auteur de la Recette
    
    INDICE = 0                                                      #Indice permettant la nivigations des Ingrédients pour la boucle 'for' 
    Taille_ingredients_recette = len(j['recipe']['ingredients'])    #Enregistrement de la taille du tableau contenant la liste des ingrédiant permettant la nivigations des Ingrédients pour la boucle 'for'
    tableau_ingredients = j['recipe']['ingredients']                #Enregistrement des ingrédients

    tableau_ingredients_affichage = j['recipe']['ingredients'][INDICE] 

    lien_auteur_recette = j['recipe']['publisher_url']              #Enregistrement de l'adresse URL de l'auteur
    appreciation_recette = j['recipe']['social_rank']               #Enregistrement du classement accordé par la communautée de http://food2fork.com/ sur le site W.E.B.
    #-----------------------------------------------------------
    
    #-----------------------------------------------------------    
    print("Informations provenant de http://food2fork.com/")                        #Message Console
    print("Les informations reçue sont en Anglais uniquement pour le moment!")      #Message Console
    print("\n")                                                                     #Saut à la ligne

    print("Une petite faim ? Voici une recette qui peut vous convenir ;=) .")       #Message Console
    print("Titre de la Recette :",Titre_recette)                                    #Affichage du Titre de la Recette
    print("\n")
    
    for INDICE in range(Taille_ingredients_recette):                                #Boucle 'for' pour navigué dans le tableau contenant les ingrédients d'une recette
        print("Les ingredients necessaires: ",j['recipe']['ingredients'][INDICE])   #Affichage des ingrédients repérer par la boucle 'for'
    
    print("\n")                                                                     #Saut à la ligne
    print("Auteur de la Recette :",auteur_recette)                                  #Affichage de l'Auteur de la Recette
    print("Lien de l'Auteur de la Recette:",lien_auteur_recette)                    #Affichage du Lien de l'Auteur de la Recette
    print("Appreciation des lecteurs",appreciation_recette,"/100")                  #Affichage du classement de la communautée de http://food2fork.com/
    #-----------------------------------------------------------
    
    return Titre_recette,INDICE,Taille_ingredients_recette,tableau_ingredients,auteur_recette,lien_auteur_recette,appreciation_recette

if __name__ == "__main__":
    get_recette()           #Fonctionnalité permettant de suggérer a l'utilisateur une recette parmis 50 013 recettes repertoriés en ligne.
