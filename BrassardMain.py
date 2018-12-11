#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Aides : http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
#Aides : http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html
#AIDES : https://www.daniweb.com/programming/software-development/threads/39554/how-to-opening-a-new-window-on-clicking-menu-item

import os
import sys
import datetime
import time

from Tkinter import * #Python Version 2
import ttk

#------------------------------------------------------------
# Add the root GPS dir so Python can find the modules
import sys
sys.path.append('/home/pi/ProjetBrassard/GPS')

from Boussole import boussole #Boussole.py
from Recuperation_Determination import determine_Brassard
from Recuperation_Determination import lecture_return_serie
from Meteo import main_meteo
from GPSoI import recuperation_coordonees_ip_brassard
from GPSoI import recuperation_coordonees_ip_brassard_V2
from emergency_number import numero_urgence
from Map_YANDEX import getMap
#------------------------------------------------------------
#------------------------------------------------------------
# Add the root Extra dir so Python can find the modules
import sys
sys.path.append('/home/pi/ProjetBrassard/Extra')

from food_suggest import get_recette
from Deezer_top_chart_suggest import top_chart_suggestion
from Deezer_top_chart import top_chart
from nettoyage_du_cache import clear_cache

from Infos_Hardware import CPU_usage
from Infos_Hardware import CPU_temp
from Infos_Hardware import SoC_info
from Infos_Hardware import MEM_info
#------------------------------------------------------------

fenetre = Tk()                                                                      #Creation d'une Fenetre Maîtresse TK appeler "fenetre"

#------------------------------------------------------------------------------     #Affichage du Temps HEURES/MINUTES/SECONDES
def temps_actuel():   
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print ("Voici l'heure:",system_time)
    return system_time
    #-- FIN -- Heure,Minute,Seconde
#---------------------------------------------
status_temps_actuel = Label(fenetre, text=temps_actuel())                   #Affichage du Temps (Label)
status_temps_actuel.pack()                                                  #Pour obtenir un affichage dynamique , Il faut utiliser pack/grid de cette façon
#---------------------------------------------
def update_temps_actuel():                                                  #Fonctionnalité permettant de mettre à jour l'Heure en fonction du Temps Réel
    # On met à jour le temps actuel dans le champs text du Widget LABEL pour afficher l'heure
    status_temps_actuel["text"] = temps_actuel()

    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_temps_actuel)    
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def information_Materiel():
    #Obtention des Informations Materiel de l'Ordinateur
    global tk_UtilisationCPU
    global tk_tk_cputemp
    global tk_MemoireUtilise

    #--        
    UtilisationCPU = CPU_usage()                                                #Obtention du Niveau d'utilisation du Processeur.
    MemoireUtilise = MEM_info()                                                 #Obtention d'information par rapport à la Memoire Vive.
    tk_cputemp = CPU_temp()                                                     #Obtention de la Temperature du Package Processeur/GPU.
    mesure_voltage,memoire_processeur,memoire_gpu  = SoC_info()                 #Obtention d'information par rapport au Couple CPU/GPU.
    
    #--

    #--Affichage--
    EnveloppeInfoMateriel = LabelFrame(fenetre, text="Informations Relatives aux Matériels", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoMateriel.pack(fill="both", expand="no")                                                        #Position de la "Zone Frame" à Label dans la fenêtre

    tk_UtilisationCPU = Label(EnveloppeInfoMateriel, text=UtilisationCPU)
    tk_MemoireUtilise = Label(EnveloppeInfoMateriel, text=MemoireUtilise)
    tk_tk_cputemp = Label(EnveloppeInfoMateriel, text=tk_cputemp)
    
    tk_UtilisationCPU.pack()
    tk_MemoireUtilise.pack()
    tk_tk_cputemp.pack()    
    #--Affichage--

def update_information_Materiel():
    #Mise a Jour des Informations a Propos du Materiel
    tk_UtilisationCPU["text"] = CPU_usage()
    tk_MemoireUtilise["text"] = MEM_info()
    tk_tk_cputemp["text"] = CPU_temp()    

    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_information_Materiel)
#---
information_Materiel() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def information_Complementaire():
    #Recuperation des Informations

    #--Numero d'Urgence--
    global tk_tk_tel_urgence    
    tk_tel_urgence = numero_urgence()
    #--Numero d'Urgence--

    
    #--Affichage--
    EnveloppeInfoComplementaire = LabelFrame(fenetre, text="Informations Complémentaires", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoComplementaire.pack(fill="both", expand="no")


    #---Affichage Numero d'Urgence---
    tk_tk_tel_urgence = Label(EnveloppeInfoComplementaire, text=tk_tel_urgence)
    tk_tk_tel_urgence.pack()
    #---Affichage Numero d'Urgence---

    
    #--Affichage--

def update_information_Complementaire():
    #Mise à Jour des Informations reçues
    tk_tk_tel_urgence["text"] = numero_urgence()

    # Après X seconde , on met à jour le contenue text du LABEL
    fenetre.after(500013, update_information_Complementaire)
#---
information_Complementaire() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
    

#------------------------------------------------------------------------------     #MENU MENU
def FenetreFood():
                                                                                    #create child window
    food = Toplevel()

                                                                                    #Reception des données
    Titre_recette,INDICE,Taille_ingredients_recette,tableau_ingredients,auteur_recette,lien_auteur_recette,appreciation_recette =get_recette()
   
                                                                                    #display message
    Titre_dela_Recette = Titre_recette
    Label(food, text="Titre de la Recette : "+Titre_dela_Recette + "\n").pack()     #Insertion des informations dans la fenêtre par le Widget "Label"

                                                                                    #Affichage des Ingrediant et Etape de la Recette a ce stade.
    for INDICE in range(Taille_ingredients_recette):                                #Boucle 'for' pour navigué dans le tableau contenant les ingrédients d'une recette  
        Label(food,text=tableau_ingredients[INDICE]).pack()                         #Affichage des ingrédients repérer par la boucle 'for'
        
    Auteur_dela_Recette = auteur_recette
    Label(food, text= "\n" + "Auteur de la Recette : "+Auteur_dela_Recette + "\n").pack()       #Insertion des informations dans la fenêtre par le Widget "Label" et son placement automatique dans la fenêtre grace a [.pack()]

    Lien_delauteur_recette = lien_auteur_recette
    Label(food, text="Lien de l'Auteur de la Recette : "+Lien_delauteur_recette + "\n").pack()  #Insertion des informations dans la fenêtre par le Widget "Label" et son placement automatique dans la fenêtre grace a [.pack()]

    appreciation_dela_recette = appreciation_recette
    Label(food, text="Appreciation des Internautes : "+ str(appreciation_dela_recette) + " sur 100" + "\n").pack()

    
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(food, text="A table!", command=food.destroy).pack()                              #Bouton permettant la fermeture de la fenêtre "food"
#---------------------------------------------
Button(fenetre, text="Quoi Manger ?", command=FenetreFood).pack()#.grid(row=3, column=10)   #Bouton permettant l'Ouverture de la Fenêtre "food"
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------     #MENU MUSIQUE
def FenetreMusique():
    # create child window
    musiquesuggest = Toplevel()

    #Récuperation des données
    Titre_Morceau,Album_Morceau,Nom_Artiste,Lien_Deezer = top_chart_suggestion()

    # display message
    Label(musiquesuggest, text="Titre du Morceau : "+ Titre_Morceau + "\n").pack() #Insertion des informations dans la fenêtre par le Widget "Label" et son placement automatique dans la fenêtre grace a [.pack()]
    Label(musiquesuggest, text="Album du Morceau : "+ Album_Morceau + "\n").pack()
    Label(musiquesuggest, text="Nom de l'Artiste : "+ Nom_Artiste + "\n").pack()
    Label(musiquesuggest, text="Lien Deezer.com : "+ Lien_Deezer + "\n").pack()

    #-------------------------
    def FenetreMusiqueTOP10():
        # create child window
        top10 = Toplevel()                                          #Création de la fenêtre enfant "top10"

        scrollbar = Scrollbar(top10)                                #Création/Déclaration d'une variable Scrollbar(dans la fenêtre top10)
        scrollbar.pack(side=RIGHT, fill=Y)                          #Placement de la Scollbar dans la fenêtre

        texte0=Text(top10, yscrollcommand=scrollbar.set)            #Déclaration du Widget "TEXT" dans la fenêtre "top10" et sa liaison avec le ScrollBar

        #Récuperation des données
        
        jdict,INDICE_TOP10,jdict['tracks']['data'][INDICE_TOP10]['position'],jdict['tracks']['data'][INDICE_TOP10]['title'],jdict['tracks']['data'][INDICE_TOP10]['album']['title'],jdict['tracks']['data'][INDICE_TOP10]['artist']['name'],jdict['tracks']['data'][INDICE_TOP10]['artist']['link'],TailleFOR_TOP10 = top_chart()

        for INDICE_TOP10 in range(TailleFOR_TOP10):                                  #Traitement à partir de 0 jusqu'a la taille de la Réponse reçu 

            texte0.insert(END,"\n" + "Information Provenant de: https://www.deezer.com/" + "\n")    #Méthode permettant l'ajout de texte

            texte0.insert(END,"\n" + "Placement TOP10: " + str(jdict['tracks']['data'][INDICE_TOP10]['position']) + "\n")

            texte0.insert(END,"\n" + "Titre du Morceau: "+jdict['tracks']['data'][INDICE_TOP10]['title'] + "\n")

            texte0.insert(END,"\n" + "Album du Morceau: "+jdict['tracks']['data'][INDICE_TOP10]['album']['title'] + "\n")

            texte0.insert(END,"\n" + "Nom de l'Artiste: "+jdict['tracks']['data'][INDICE_TOP10]['artist']['name'] + "\n")

            texte0.insert(END,"\n" + "Lien Deezer.com: "+ jdict['tracks']['data'][INDICE_TOP10]['artist']['link'] + "\n" + "\n")

            texte0.pack(side=LEFT, fill=BOTH, expand=True)                          #Instruction permettant le placement du Widget "TEXT" dans la fenêtre (Côté Gauche,Rempli,Rempli l'espace laissé disponible par le reste des autre Widgets dans la même fenêtre)

            scrollbar.config(command=texte0.yview)                                  #Contrôle de La ScrollBar


        Button(top10,text="Merci.",command=top10.destroy).pack()                                    #Bouton pour fermer la fenêtre "top10"
    #-------------------------
            
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    Button(musiquesuggest, text="A l'écoute!", command=musiquesuggest.destroy).pack()               #Bouton permettant de fermer la fenêtre "musiquesuggest"
    Button(musiquesuggest, text="Accéder au Top10", command=FenetreMusiqueTOP10).pack()             #Bouton pour Accéder à la fenêtre "top10"
#---------------------------------------------
Button(fenetre, text="Quoi ecouter ?", command=FenetreMusique).pack() #.grid(row=4, column=10)      #Bouton pour Ouvrir la fenêtre "musiquesuggest"
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------     #MENU METEO
#Cette fonction permet d'avoir une fenetre ENFANT pour l'affichage du Menu Meteo
def FenetreGPS():
    #Recuperation de la Variable "Validite"
    Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere, = lecture_return_serie() #Récuperation des variables depuis le fichier Python "Recuperation_Determination"

    #Créer une fenêtre fille
    global GPS
    global GPSErreur

    #---Zone de Test de Conformité de la Trame GPS reçue pour l'Affichage---
    #Si la Trame est Refusé dans ce cas On affiche deux Messages , un affichage standars plus la Variable testé et dans le cas contraire le programme continue sont Exécution normal.
    #Validite = "V" #Valeur de TEST

    if Validite == "V":
        GPS = None                  #La Fenêtre GPS ne sera pas définition en cas de Non conformité de la Trame NMEA GPS
        GPSErreur = Toplevel()      #Définition de la Fenêtre en GPSErreur en cas de Non conformite de la Trame 
        Label_Annonce_GPSErreur = Label(GPSErreur,text="Malheureusement, Nous ne captons pas correctement le Signal G.P.S , déplacez vous ;=)") #Affichage d'un Message d'Erreur textuel
        Label_Annonce_GPSErreur.pack()                                          #Placement dans l'espace alouable
        Label_ShowValue_GPSErreur = Label(GPSErreur, text=Validite)             #Affichage de la Valeur 'Validite' reçu par le Stick G.P.S
        Label_ShowValue_GPSErreur.pack()                                        #Placement de cette Valeur dans l'espace alouable de la Fenêtre
        print("La Trame recu n'est pas Valide // Validite = V :", Validite)     #Affichage d'un message d'erreur + de la Valeur 'Validite' dans la Console

        def ProgressBar_refresh_GPSErreur():                                    #Fonctionnalité permettant d'afficher une petite Barre de Chargement pour faire attendre l'Utilisateur , cette bar changera de comportement en fonction de la conformité de la Trame G.P.S.
            #Recuperation de la Variable "Validite"
            Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere, = lecture_return_serie() #Récuperation des variables depuis le fichier Python "Recuperation_Determination"
            
            #---PROGRESSBAR TTK---
            #Aides: https://gist.github.com/kochie/9f0b60384ccc1ab434eb
            ft = ttk.Frame(GPSErreur)                                               #Utilisation d'un Widget TTK , dans notre cas "ProgressBar" et placement dans la Fenêtre GPSErreur 
            ft.pack(expand=False, fill="both", side="top")                          #Placement du Widget dans l'espace
            pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')  #Specification du Widget
            pb_hD.pack(expand=False, fill="both", side="top")                       #Information de Placement du Widget dans l'espce supplémentaire

            Validite_ProgressBar = Validite                                         #Mise à Jour de la Validite

            if Validite_ProgressBar =='A':                                          #Si la Validite est Conforme alors...
                pb_hD.start(3)                                                      #...La ProgressBar s'agite
            else:
                pb_hD.start(50)                                                     #Sinon, la ProgressBar ralenti.
            #---PROGRESSBAR TTK---
                
        def update_refresh_GPSErreur():                                         #Fonctionnalité permettant de mettre à jour le Message d'Erreur en fonction de l'état de la Conformité du Signal G.P.S.
            #Recuperation de la Variable "Validite"
            Decimal_latitude,Decimal_longitude,Validite,Latitude_Hemisphere,Longitude_Hemisphere, = lecture_return_serie() #Récuperation des variables depuis le fichier Python "Recuperation_Determination"
            
            # On met à jour la Valeur VALIDITE dans le champs text d Widget LABEL pour l'afficher
            Label_ShowValue_GPSErreur["text"] = Validite
            if Validite =="A":
                Label_Annonce_GPSErreur["text"] = "Le Signal GPS à été retrouvé, Vous pouvez Fermer cette Fenêtre et Relancer le GPS"
            else :
                Label_Annonce_GPSErreur["text"] = "Le Signal GPS à été perdue, Vous pouvez utilisez le Bouton en dessous pour vérifier l'état du Signal de Nouveau ; Déplacez-Vous ;=)"

            # Après X secondes , on met à jour le contenue text du LABEL
            GPSErreur.after(5000, update_refresh_GPSErreur)

        ProgressBar_refresh_GPSErreur()                                                                 #Execution de la Bar de Chargement
        Button(GPSErreur, text="Vérifier une Nouvelle Fois ?", command=update_refresh_GPSErreur).pack() #Bouton permettant de Vérifier une nouvelle fois la conformité du Signal à l'instant
        Button(GPSErreur, text="Fermer", command=GPSErreur.destroy).pack()                              #Bouton permettant de Fermer la Fenêtre
        

    else : #if Validite == "A": Si le Signal est conforme , le Reste du Programme s'execute normalement
        print("La Trame recu est Valide // Validite = A :", Validite)        
        GPS=Toplevel()
    #---Zone de Test de Conformité de la Trame GPS reçue pour l'Affichage---

    #Récuperation des données
    #-----Bousole-----
    round_retourne_latitude,dir_Latitude_Hemisphere,round_retourne_longitude,dir_Longitude_Hemisphere = boussole()
    #-----Bousole-----

    #-----Récuperation_Determination-----
    Ville,Numero_Maison,Rue,Code_Postal,Pays = determine_Brassard()
    #-----Récuperation_Determination-----

    #-----Météo-----
    tk_status_climat,tk_climat_min,tk_climat_now,tk_climat_max,tk_vitesse_du_vent,tk_volume_de_neige,tk_volume_de_pluie,tk_pourcentage_humidite,tk_couverture_de_nuage = main_meteo()
    #-----Météo-----
    
    # display message                                                               #Affichage d'un Message (Informations)

    #---Affichage BOUSSOLE---    
    EnveloppeGPS = LabelFrame(GPS, text="Boussole Numérique", padx=5, pady=5)   #Création d'une "Zone Frame" à Label
    EnveloppeGPS.pack(fill="both", expand="no")                                 #Position de la "Zone Frame" à Label dans la fenêtre
    
    LabelEnveloppeGPS = Label(EnveloppeGPS, text=boussole())                    #Création du Label et insertion de sa valeur
    LabelEnveloppeGPS.pack()                                                    #Positionement du Label dans la Fenêtre
    #---Affichage BOUSSOLE---

    #---Affichage Récuperation_Determination---
    EnveloppeRD = LabelFrame(GPS, text="Coordonées Physiques", padx=5, pady=5)  #Création d'une "Zone Frame" à Label
    EnveloppeRD.pack(fill="both", expand="no")                                  #Position de la "Zone Frame" à Label dans la fenêtre
    
    LabelEnveloppeRD = Label(EnveloppeRD, text=determine_Brassard())            #Création du Label et insertion de sa valeur
    LabelEnveloppeRD.pack()                                                     #Positionement du Label dans la Fenêtre
    #---Affichage Récuperation_Determination---

    #---Affichage Météo---
    EnveloppeMeteo = LabelFrame(GPS, text="Informations Météorologiques aux Coordonées", padx=5, pady=5)   #Création d'une "Zone Frame" à Label
    EnveloppeMeteo.pack(fill="both", expand="no")                                           #Position de la "Zone Frame" à Label dans la fenêtre

    tk_status_climat_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_status_climat)
    tk_climat_min_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_climat_min)                          #Création du Label et insertion de sa valeur
    tk_climat_now_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_climat_now)
    tk_climat_max_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_climat_max)
    tk_vitesse_du_vent_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_vitesse_du_vent)
    tk_volume_de_neige_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_volume_de_neige)
    tk_volume_de_pluie_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_volume_de_pluie)
    tk_pourcentage_humidite_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_pourcentage_humidite)
    tk_couverture_de_nuage_LabelEnveloppeMeteo = Label(EnveloppeMeteo, text=tk_couverture_de_nuage)

    tk_status_climat_LabelEnveloppeMeteo.pack()
    tk_climat_min_LabelEnveloppeMeteo.pack()                                                                #Placement des Valeurs dans l'espace alouable de la Fenêtre
    tk_climat_now_LabelEnveloppeMeteo.pack()
    tk_climat_max_LabelEnveloppeMeteo.pack()
    tk_vitesse_du_vent_LabelEnveloppeMeteo.pack()
    tk_volume_de_neige_LabelEnveloppeMeteo.pack()
    tk_volume_de_pluie_LabelEnveloppeMeteo.pack()
    tk_pourcentage_humidite_LabelEnveloppeMeteo.pack()
    tk_couverture_de_nuage_LabelEnveloppeMeteo.pack()
    #---Affichage Météo--- 

    
    #---Raffaichissement Boussole---
    def update_refresh_Boussole():                                                  #Fonctionnalité permettant de mettre à jour la Boussole Numérique

        # On met à jour la Boussole dans le champs text du Widget LABEL pour l'afficher
        LabelEnveloppeGPS["text"] = boussole()

        # Après X secondes , on met à jour le contenue text du LABEL
        GPS.after(10000, update_refresh_Boussole)    
    #---Raffaichissement Boussole---

    #---Raffaichissement Boussole---
    def update_refresh_RD():                                                  #Fonctionnalité permettant de mettre à jour les Coordonées Physiques

        # On met à jour les coordonées dans le champs text du Widget LABEL pour l'afficher
        LabelEnveloppeRD["text"] = determine_Brassard()

        # Après X secondes , on met à jour le contenue text du LABEL
        GPS.after(23000, update_refresh_RD)    
    #---Raffaichissement Boussole---

    #---Raffaichissement Météo---
    def update_refresh_Meteo():                                                  #Fonctionnalité permettant de mettre à jour les Coordonées Physiques
        
        # On met à jour les informations dans le champs text du Widget LABEL pour l'afficher
        tk_status_climat_LabelEnveloppeMeteo["text"],tk_climat_min_LabelEnveloppeMeteo["text"],tk_climat_now_LabelEnveloppeMeteo["text"],tk_climat_max_LabelEnveloppeMeteo["text"],tk_vitesse_du_vent_LabelEnveloppeMeteo["text"],tk_volume_de_neige_LabelEnveloppeMeteo["text"],tk_volume_de_pluie_LabelEnveloppeMeteo["text"],tk_pourcentage_humidite_LabelEnveloppeMeteo["text"],tk_couverture_de_nuage_LabelEnveloppeMeteo["text"] = main_meteo()
        
        # Après X secondes , on met à jour le contenue text du LABEL
        GPS.after(330000, update_refresh_Meteo)  
    #---Raffaichissement Météo---

    #---GPSoI_tkinter---
    #Dans cette fonctionnalite nous combinons de Service de Localisation d'adresse IP pour obtenir le plus d'informations sur l'adresse IP de l'Utilisateur
    def GPSoI_tkinter():
        global GPSoI_tkinter_window
        GPSoI_tkinter_window = Toplevel()

        #Récuperation des Information
        ip_GPSoI,latitude_GPSoI,longitude_GPSoI,city_GPSoI,region_name_GPSoI,ZIP_GPSoI,country_name_GPSoI,continent_name_GPSoI = recuperation_coordonees_ip_brassard()  #SERVICE NUMERO UN
        tkk_ip,tkk_hostname,tkk_org,tkk_loc,tkk_city,tkk_region,tkk_country = recuperation_coordonees_ip_brassard_V2()                                                  #SERVICE NUMERO DEUX
    
        #Zone d'affichage
        EnveloppeGPSoI = LabelFrame(GPSoI_tkinter_window, text="Informations Relatives à votre Adresse IP Publique", padx=5, pady=5)   #Création d'une "Zone Frame" à Label
        EnveloppeGPSoI.pack(fill="both", expand="no")                                           #Position de la "Zone Frame" à Label dans la fenêtre
        
        #Affichage des Informations Recues
        tk_ip_GPSoI = Label(EnveloppeGPSoI, text=ip_GPSoI)    
        tkk_hostnameV2 = Label(EnveloppeGPSoI, text=tkk_hostname)
        tkk_locV2 = Label(EnveloppeGPSoI, text=tkk_loc)
        tk_latitude_GPSoI = Label(EnveloppeGPSoI, text=latitude_GPSoI)
        tk_longitude_GPSoI = Label(EnveloppeGPSoI, text=longitude_GPSoI)
        tk_city_GPSoI = Label(EnveloppeGPSoI, text=city_GPSoI)
        tk_region_name_GPSoI = Label(EnveloppeGPSoI, text=region_name_GPSoI)
        tk_ZIP_GPSoI = Label(EnveloppeGPSoI, text=ZIP_GPSoI)
        tk_country_name_GPSoI = Label(EnveloppeGPSoI, text=country_name_GPSoI)
        tk_continent_name_GPSoI = Label(EnveloppeGPSoI, text=continent_name_GPSoI)

        tk_ip_GPSoI.pack()
        tkk_hostnameV2.pack()
        tkk_locV2.pack()
        tk_latitude_GPSoI.pack()
        tk_longitude_GPSoI.pack()
        tk_city_GPSoI.pack()
        tk_region_name_GPSoI.pack()
        tk_ZIP_GPSoI.pack()
        tk_country_name_GPSoI.pack()
        tk_continent_name_GPSoI.pack()

        #--UPDATE--
        def GPSoI_tkinter_update():
            # On met à jour les informations dans le champs text du Widget LABEL pour l'afficher
            tk_ip_GPSoI["text"],tk_latitude_GPSoI["text"],tk_longitude_GPSoI["text"],tk_city_GPSoI["text"],tk_region_name_GPSoI["text"],tk_ZIP_GPSoI["text"],tk_country_name_GPSoI["text"],tk_continent_name_GPSoI["text"] = recuperation_coordonees_ip_brassard()
            tkk_ip,tkk_hostnameV2["text"],tkk_locV2["text"],tkk_loc,tkk_city,tkk_region,tkk_country = recuperation_coordonees_ip_brassard_V2() 
            #Actualisation des ChAMPS text uniquement.
    
            # Après X secondes , on met à jour le contenue text du LABEL
            GPSoI_tkinter_window.after(130000, GPSoI_tkinter_update)
        #--UPDATE--
            
        GPSoI_tkinter_update() #Fonctionnalité permettant de mettre à jours dans l'interface les informations en rapport avec l'Adresse IP de l'Utilisateur
        
        Button(GPSoI_tkinter_window, text="MAJ Infos IP Publique", command= GPSoI_tkinter_update).pack()
        Button(GPSoI_tkinter_window, text="Fermer", command=GPSoI_tkinter_window.destroy).pack()
    #---GPSoI_tkinter---
        
    #---MAP YANDEX---
    def Show_MAP():
        #AIDES: http://tkinter.fdex.eu/doc/uwm.html#update_idletasks
        #AIDES: https://stackoverflow.com/questions/19838972/how-to-update-an-image-on-a-canvas/19842646
        
        #Dans cette fonctionnalitee nous allons obtenir une carte ou ce situe l'utilisateur du Logiciel.
        global Show_YANDEXMAP
        #global MAPjpg
        Show_YANDEXMAP = Toplevel()

        #Execution du script Python permettant la recuperation de la carte et Recuperation de l'emplacement de la carte dans l'ordinateur
        getMap()
        
        #Zone d'affichage
        EnveloppeMAP = LabelFrame(Show_YANDEXMAP, text="Votre Position Geographique", padx=5, pady=5)   #Création d'une "Zone Frame" à Label
        EnveloppeMAP.pack(fill="both", expand="no")                                                     #Position de la "Zone Frame" à Label dans la fenêtre

        canvas = Canvas(EnveloppeMAP,width=600, height=300, bg='black')                         #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)

        canvas.pack(expand=NO, fill=None)                                                       #Placement du CANVAS de l'espace

        MAPjpg = PhotoImage(file="/home/pi/ProjetBrassard/GPS/MAP_downloads/map.jpg")           #Chargement de la MAP

        canvas.file = MAPjpg                                                                    #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
    
        image_on_canvas = canvas.create_image(0,0,image=MAPjpg , anchor=NW)                     #Integration de la MAP

        #--UPDATE--
        def update_refresh_Show_MAP():
            print("Mise a Jour de la Cartographie Geographique")                            #Message dans la Console
            getMap()                                                                        #Obtention d'une Nouvelle Cartographie
            MAPjpg = PhotoImage(file="/home/pi/ProjetBrassard/GPS/MAP_downloads/map.jpg")   #Chargement de la MAP
            canvas.file = MAPjpg                                                            #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
            canvas.itemconfig(image_on_canvas,image= MAPjpg)                                #Permet la mise a jour de l'image
             # Après X secondes , on met à jour le contenue text du LABEL
            Show_YANDEXMAP.after(3000, update_refresh_Show_MAP)
        #--UPDATE--

        update_refresh_Show_MAP()   #Fonctionnalité permettant de mettre à jours dans l'interface la Carte Geographique de la position de l'Utilisateur
        Button(Show_YANDEXMAP, text="Fermer", command=Show_YANDEXMAP.destroy).pack()  #Bouton de Fermeture du Programme        
    #---MAP YANDEX---

    update_refresh_Boussole()   #Fonctionnalité permettant de mettre à jours dans l'interface la Boussole Numérique
    update_refresh_RD()         #Fonctionnalité permettant de mettre à jours dans l'interface les Coordonées Physiques
    update_refresh_Meteo()      #Fonctionnalité permettant de mettre à jours dans l'interface les informations Météorologiques    
    
    Button(GPS, text="Re-Lancer la Boussole", command=update_refresh_Boussole).pack()                  #Bouton pour Lancer la Mise à Jour de la Boussole
    Button(GPS, text="MAJ les Coordonées Physiques", command=update_refresh_RD).pack()                  #Bouton pour Lancer la Mise à Jour de la Boussole
    Button(GPS, text="Votre Position sur la MAP", command=Show_MAP).pack()
    Button(GPS, text="MAJ La Meteo", command=update_refresh_Meteo).pack()

    Button(GPS, text="Infos IP Publique", command= GPSoI_tkinter).pack()

    Button(GPS, text="Fermer", command=GPS.destroy).pack()                                             #Bouton pour quitter la page "GPS" 
#---------------------------------------------
#Bouton Meteo permettant d'utilisé la fonction "FenetreMeteo()"
Button(fenetre, text="G.P.S", command=FenetreGPS).pack() #.grid(row=3, column=0) #Bouton pour Ouvrir la page "meteo"
#------------------------------------------------------------------------------

#-------------------------------------Clavier Virtuel-----------------------------------------
def lance_clavier():
    print("Lancement du Clavier Virtuel") 
    #os.system("matchbox-keyboard &")   #sudo apt-get install matchbox-keyboard
    os.system("florence &")             #sudo apt-get install florence && sudo apt-get install at-spi2-core
#-------------------------------------Clavier Virtuel-----------------------------------------

#------------------------------------------------------------------------------     
Button(fenetre,text="Nettoyage du Cache", command=clear_cache).pack()
Button(fenetre, text="Clavier Virtuel", command=lance_clavier).pack()
boutonclose=Button(fenetre, text="Fermer", command=fenetre.quit).pack() #.grid(row=13, column=13)    #BOUTON DE CLÔTURE DE LA FENÊTRE PRINCIPALE
#------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        clear_cache()
        lance_clavier()

        #Récupération des informations pour la Mise à jour du LABEL toute les 1 milliseconde quand la fenêtre Maitre est lancée
        fenetre.after(1, update_temps_actuel)               #update_temps_actuel()
        fenetre.after(1, update_information_Materiel)       #update_information_Materiel()
        #fenetre.after(1, update_information_Complementaire) #update_information_Complementaire()

        fenetre.mainloop()                                  #Boucle de Lancement de la Fenêtre PRINCIPAL

        GPSErreur.after(1,ProgressBar_refresh_GPSErreur)    #ProgressBar_refresh_GPSErreur()
        GPSErreur.after(1,update_refresh_GPSErreur)         #update_refresh_GPSErreur()

        GPS.after(1,update_refresh_Boussole)                #update_refresh_Boussole()
        GPS.after(2,update_refresh_RD)                      #update_refresh_RD()
        GPS.after(3,update_refresh_Meteo)                   #update_refresh_Meteo()

        GPSoI_tkinter_window.after(4,GPSoI_tkinter_update)  #GPSoI_tkinter_update()

        Show_YANDEXMAP.after(5,update_refresh_Show_MAP)     #update_refresh_Show_MAP()
        
        pass

    except TypeError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console                              
	print("Code Erreur: TypeError")
        clear_cache()

    except KeyError:
	print("API Geocoder a planté, il faut recommencer une nouvelle fois ;=)")                    #On affiche ce message dans la console                              
	print("Code Erreur: KeyError")
        clear_cache()
        
    except ValueError:
	print("Le signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: ValueError")
        clear_cache()
    except AssertionError:
	print("Le Signal GPS est degradé , veuillez-vous deplacez!")                    #On affiche ce message dans la console
        print("Code Erreur: AssertionError")
        clear_cache()
    except NameError:
	print("Il est necessaire de Redemarrez le GPS!")                                #On affiche ce message dans la console
        print("Code Erreur: NameError")
        clear_cache()
    except:
	print("Il est necessaire de Redemarrez le Logiciel!")                                #On affiche ce message dans la console
        print("Code Erreur: Aucun")
        clear_cache()
                                                                         #---!!!GESTION DES ERREURS!!!---


    
