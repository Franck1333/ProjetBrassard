#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Aides : http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
#Aides : https://psutil.readthedocs.io/en/latest/index.html
#AIDES : https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python

import os
import sys
import datetime
import time

from nettoyage_du_cache import clear_cache
import psutil


def psutil_CPU():    
    print("Indique le Nombre de Coeurs Physique/Logique Présent")
    psutil.cpu_count()

    print("Utilisation du CPU affiché en Pourcentage")
    psutil.cpu_percent(interval=0.1)
    
    #print("Indication des Fréquence d'Horloges Utilisées : Actuel,Min,Max.")
    #psutil.cpu_freq()




if __name__ == "__main__":
    clear_cache()
    psutil_CPU()
