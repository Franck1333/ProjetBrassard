#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Aides : https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item
#Aides : http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel

import urllib       #Blibliotheque permetant de recuperer une ou plusieurs ressources sur Internet via HTTP/HTTPS
from Tkinter import *
from Recuperation_Determination import lecture_return_serie
from nettoyage_du_cache import clear_cache

def getMap():
    #---Service---#
    print('Telechargement de la Carte/Map .jpg')            #Message dans la Console

    latitude,longitude,Validite,dir_Latitude_Hemisphere,dir_Longitude_Hemisphere, = lecture_return_serie()

    print(latitude)
    print(longitude)

    url = "https://static-maps.yandex.ru/1.x/?lang=en-US&ll="+str(longitude)+","+str(latitude)+"&z=16&l=skl,map,trf&size=600,300&pt="+str(longitude)+","+str(latitude)+",flag"  #URL utilise pour obtenir la carte 
    #Ce service de MAP STATIC ce nomme YANDEX
    #Nous l'utilisons de cette facon : https://static-maps.yandex.ru/1.x/?lang=en-US&ll=LONGITUDE,LATITUDE&z=13&l=skl,map,trf&size=600,300&pt=LONGITUDE,LATITUDE,flag

    urllib.urlretrieve(url, '/home/pi/ProjetBrassard/GPS/MAP_downloads/map.jpg')   #Telechargement de l'image resultant de la requete
    #---Service---#


def getMapInterface():
    #---Interface---#

    #import Tkinter as tk
    #tk.NoDefaultRoot

    print('Affichage de la Carte/Map .jpg Telechargee')            #Message dans la Console

    fenetre = Tk()

    #Zone d'affichage
    EnveloppeMAP = LabelFrame(fenetre, text="Votre Position Geographique", padx=5, pady=5)   #Création d'une "Zone Frame" à Label
    EnveloppeMAP.pack(fill="both", expand="no")                                           #Position de la "Zone Frame" à Label dans la fenêtre

    canvas = Canvas(EnveloppeMAP,width=600, height=300, bg='black')  #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)

    canvas.pack(expand=NO, fill=None)                          #Placement du CANVAS de l'espace

    MAPjpg = PhotoImage(file='/home/pi/ProjetBrassard/GPS/MAP_downloads/map.jpg')      #Chargement de la MAP

    canvas.create_image(0,0,image=MAPjpg,anchor=NW)             #Integration de la MAP

    Button(fenetre, text="Fermer", command=fenetre.destroy).pack()  #Bouton de Fermeture du Programme

    fenetre.mainloop()                                              #Lancement du Programme Principal
    #---interface---#

if __name__ == "__main__":
    getMap()
    getMapInterface()
    clear_cache()
    
