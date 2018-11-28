#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides : https://pypi.org/project/weather-api/

import serial
import time
import os
import sys

from Recuperation_Determination import meteo
from Recuperation_Determination import determine_less

from nettoyage_du_cache import clear_cache

import pyowm        #API pour la Météo
import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents; Utilisation: unicodedata.normalize('NFKD', ville).encode('ASCII', 'ignore')

#-----------------------------------------------------------------------------------------------------------------------------------
def main_meteo_3h():

    #-----------------------------------------------------------------------------
    owm = pyowm.OWM('7435ea1b7ee5e31fe1f524a922202510',language = "en") #Clé d'accès API
    meteo()                                                             #MAIN DU FICHIER Recuperation_Determination.py permettant de lancer la capture des infomations provenant du STICK GPS
    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------
    ville = determine_less()                                                        #Obtention de la ville grâce a la fonction determine_less() du fichier Recuperation_Determination.py
    global ville_encode
    ville_encode = unicodedata.normalize('NFKD', ville).encode('ASCII', 'ignore')   #On enregistre la ville en retirant les accents de la langue 
    print("Ville en version sans accent:",ville_encode)                             #Affichage dans la console
    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------
    fc = owm.three_hours_forecast(ville_encode)                                     #On donne la ville sans accent à la méthode permettant la recherche des informations pour une prévisions sur 3 Heures
    #fc = owm.three_hours_forecast("Osaka")

    will_pluie = fc.will_have_rain()    #Variable de Type Boolean permettant de Savoir si Oui/Non , il y a de la Pluie prevue pour les 3 prochaines Heures
    will_soleil = fc.will_have_sun()    #Variable de Type Boolean permettant de Savoir si Oui/Non , il y a du Soleil prevue pour les 3 prochaines Heures
    will_snow = fc.will_have_snow()     #Variable de Type Boolean permettant de Savoir si Oui/Non , il y a de la Neige prevue pour les 3 prochaines Heures

    #print(will_pluie)
    #print(will_soleil)
    #print(will_snow)
    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------
    if will_pluie == True :                                                     #Si il y a de la pluie alors...
        print("Dans les 3 prochaines Heures, de la Pluie est prevue!")          #On affirme cela par un message dans la console
    elif will_pluie == False :                                                  #Sinon...
        print("Aucune Pluie n'est prevue pour les 3 prochaines Heures")         #Un message Négatif sera lisible dans la console

    if will_soleil == True :
        print("Dans les 3 prochaines Heures, du Soleil est prévue!")
    elif will_soleil == False :
        print("Aucun Rayon de Soleil n'est prevue pour les 3 prochaines Heures")
    
    if will_snow == True :
        print("Dans les 3 prochaines Heures, de la Neige est prévue!")
    elif will_snow == False :
        print("Aucun Flocon de Neige n'est prevue pour les 3 prochaines Heures")

    return will_pluie,will_soleil,will_snow                                     #On retourne ces trois booléan , pour une autre utilisation de ces données.
    #-----------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------
def confirme_erreur_ville(): #Fonction simple permettant de mettre un booléan à True si il y a une erreur de la recherche d'une Ville
    global erreur_ville
    erreur_ville = True

    return erreur_ville      #Retourne le Booléan
    #-----------------------------------
    
    
if __name__ == "__main__":
    clear_cache()                                                       #Nettoyage des Fichiers caches PYTHON
    #-----------------------------------
    try:                                                                #---!!!GESTION DES ERREURS!!!---
        main_meteo_3h()                                                                 #On lance le programme meteo avec precision sur 3 heures ,Lancement de la fonction principale
        pass                                                                            #Si le tout fonctionne alors on continue
    except TypeError:                                                                   #Si il y a eu une erreur de TYPE de variables alors...
        print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: TypeError")                                                 #Affichage Code Erreur Correspondant
    except pyowm.exceptions.api_response_error.NotFoundError:                              #Si la recherche n'a donné aucun résultat alors
        confirme_erreur_ville()                                                         #On met un booléan a la valeur True
        print("La ville ou vous situez",ville_encode,", n'a pas ete trouver!")          #Et on affiche un message dans la console
        print("Code Erreur: pyowm.exceptions.not_found_error.NotFoundError // pyowm.exceptions.api_response_error.NotFoundError")            #Affichage Code Erreur Correspondant
                                                                        #---!!!GESTION DES ERREURS!!!---
    #-----------------------------------
