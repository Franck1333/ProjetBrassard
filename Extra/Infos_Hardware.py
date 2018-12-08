#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AIDES: https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-sage-e-g-57-on-linux
#AIDES: https://stackoverflow.com/questions/10585978/linux-command-for-percentage-of-memory-that-is-free
#AIDES: https://docs.python.org/2/library/commands.html
import os
import sys
import datetime
import time
from nettoyage_du_cache import clear_cache


import io
import commands


def CPU_usage():
    #Charge CPU
    global UtilisationCPU

    LectureCommande0=commands.getoutput("top -bn 1 | awk 'NR>7{s+=$9} END {print s/4}'")    #On execute cette commande pour Obtenir le resultat depuis le sysytem sans passer par un programme tièrce
    UtilisationCPU = "Utilisation du Processeur: " + LectureCommande0 + " %"                #Enregistrement de la Variable reçu et Mise en forme
    print(UtilisationCPU)                                                                   #Affichage des nouvelles données reçu dans la console

    return UtilisationCPU                                                       #Retourne les valeurs pour une prochaine utilisation.

def CPU_temp():
    #Temperature du CPU/SoC
    global tk_cputemp
        #f = open("/sys/class/thermal/thermal_zone0/temp")
        #t = f.readline ()
        #cputemp = "CPU temp: "+t
    cputemp = commands.getoutput("vcgencmd measure_temp")
    print ("Temperature du Processeur: "+ cputemp)

    #--
    tk_cputemp        = "Temperature du Processeur: " + cputemp                             #Mise en forme pour l'affichage sous Tkinter
    #--

    return tk_cputemp 

def SoC_info():
    global mesure_voltage
    global memoire_processeur
    global memoire_gpu

    #Voltage utilisé par le Socket CPU/GPU
    LectureCommande1=commands.getoutput("vcgencmd measure_volts core")
    mesure_voltage = "Tension utilisé par l'ensemble CPU/GPU: " + LectureCommande1 
    print(mesure_voltage)

    #Indication de la Mémoire Vive alouée pour le Processeur
    LectureCommande2=commands.getoutput("vcgencmd get_mem arm")
    memoire_processeur = "Mémoire Vive alouée pour le Processeur: " + LectureCommande2 
    print(memoire_processeur)

    #Indication de la Mémoire Vive alouée pour le Processeur Graphique
    LectureCommande3=commands.getoutput("vcgencmd get_mem gpu")
    memoire_gpu = "Mémoire Vive alouée pour le Processeur Graphique: " + LectureCommande3 
    print(memoire_gpu)

    return mesure_voltage,memoire_processeur,memoire_gpu   

def MEM_info():
    #Charge Memoire Vive
    global MemoireUtilise
    LectureCommande4=commands.getoutput("free | grep Mem | awk '{print $3/$2 * 100.0}'")
    MemoireUtilise = "Memoire Vive Utilise: " + LectureCommande4 + " %"
    print(MemoireUtilise)

    return MemoireUtilise


if __name__ == "__main__":
    clear_cache()           #Nettoyage du Cache Python.
    CPU_usage()             #Obtention du Niveau d'utilisation du Processeur.
    CPU_temp()              #Obtention de la Temperature du Processeur.
    SoC_info()              #Obtention d'information par rapport au Couple CPU/GPU.
    MEM_info()              #Obtention d'information par rapport à la Memoire Vive.
