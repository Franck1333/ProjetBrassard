#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Liste les Numéros de Téléphone d'Urgence du Monde entiers
#L'Amérique : 911
#L'Europe   : 112
#L'Asie     : 110 ou 119
#Reste du Monde : 999
#Si le continent n'est pas trouvé : 112 ou 911 ou 999

#------------------------------------------------------------
from GPSoI import recuperation_coordonees_ip
#------------------------------------------------------------
#from GPSoI import recuperation_coordonees_ip    #Nous utilisons la localisation de l'Adresse IP de l'utilisateur pour localiser son continent actuel pour lui transmettre les informations correspondant a sa localisation

from nettoyage_du_cache import clear_cache
import unicodedata #Cette blibliothèque permet de travailler avec du contenue contenant des accents

def numero_urgence():

    nom_continent,latitude,longitude = recuperation_coordonees_ip()                                                        #Obtention du continent de l'utilisateur
    
    emergency_phone_number = {}                                                                         #Déclaration d'un Nouveau Dictionnaire

    emergency_phone_number["Europe"] = "112"                                                            #Dictionnaire avec comme clé "Europe"
    emergency_phone_number["America"] = "911"                                                           #Dictionnaire avec comme clé "America"
    emergency_phone_number["Asia"] = "110 or 119"                                                       #Dictionnaire avec comme clé "Asia"                                                       
    emergency_phone_number["Africa"] = "107"                                                            #Dictionnaire avec comme clé "Africa"
    emergency_phone_number["Antarctica"] = "911 or 112"                                                 #Dictionnaire avec comme clé "Antarctica"
    emergency_phone_number["Oceania"] = "000 or 911 "                                                   #Dictionnaire avec comme clé "Oceania"
    emergency_phone_number["Eurasia"] = "112 or 110"                                                    #Dictionnaire avec comme clé "Eurasia"
    emergency_phone_number["North America"] = "112 or 911"                                              #Dictionnaire avec comme clé "North America"
    emergency_phone_number["Central America"] = "112 or 911"                                            #Dictionnaire avec comme clé "Central America"
    emergency_phone_number["South America"] = "112 or 911 or 999"                                       #Dictionnaire avec comme clé "South America"
    emergency_phone_number["Caribbean"] = "911 or 112 or 999"                                           #Dictionnaire avec comme clé "Caribbean"
    
    #print("Numéro d'Urgence Pour l'Europe:",emergency_phone_number["Europe"])
    #print("Numéro d'Urgence Pour l'Amérique:",emergency_phone_number["America"])
    #print("Numéros d'Urgences Pour l'Asie:",emergency_phone_number["Asia"])
    #print("Numéro d'Urgence Pour l'Afrique:",emergency_phone_number["Africa"])
    #print("Numéros d'Urgences Pour l'Antarctique:",emergency_phone_number["Antarctica"])
    #print("Numéros d'Urgences Pour l'Océanie:",emergency_phone_number["Oceania"])
    #print("Numéros d'Urgences Pour l'Eurasie:",emergency_phone_number["Eurasia"])
    #print("Numéros d'Urgences Pour l'Amérique du Nord:",emergency_phone_number["North America"])
    #print("Numéros d'Urgences Pour l'Amérique Centrale:",emergency_phone_number["Central America"])
    #print("Numéros d'Urgences Pour l'Amérique du Sud:",emergency_phone_number["South America"])
    #print("Numéros d'Urgences Pour Les Caraïbes:",emergency_phone_number["Caribbean"])

    print("En cas de problème grave,voici les Numéros de Téléphone d'Urgence à composer disponible sur votre continent.")   #Message Console Informations
    print("Pour",nom_continent)                                                                                             #Message Console indiquant le continent
    print("Numeros d'Urgence disponible pour votre Region:",emergency_phone_number[nom_continent])                          #Message Console indiquant le numéro d'urgence à composer

    tel_urgence = emergency_phone_number[nom_continent]                                                                     #Enregistrment du numéro d'urgence dans une variable en fonction de la localisation de l'utilisateur

    #print(tel_urgence) #Numero(s) de Telephone(s) determiné(s) #TEST - DEBUG

    tk_tel_urgence = "Le(s) Numero(s) d'Urgence(s) dans votre continent: " + str(tel_urgence)

    return tk_tel_urgence                                                                                                      #Retourne le numéro de Téléphone d'Urgence


if __name__ == "__main__":
    clear_cache()
    numero_urgence()   #Programme permettant de connaitre le ou les numéros d'Urgence en cas de problème correspondant à la localisation du contient exacte de l'Adresse IP de l'utilisateur
