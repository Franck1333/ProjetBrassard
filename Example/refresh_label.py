status_temps_actuel = Label(fenetre, text=temps_actuel())                   #Affichage du Temps (Label)
status_temps_actuel.pack()                                                  #Pour obtenir un affichage dynamique , Il faut utiliser pack/grid de cette façon
#---------------------------------------------
def update_temps_actuel():                                                  #Fonctionnalité permettant de mettre à jour l'Heure en fonction du Temps Réel
    # Obtention de L'heure du demarrage du Programmme
    current_status = status_temps_actuel["text"]
    
    # Si le message actuel est différent de temps_actuel() alors on récupere temps_actuel une seconde fois
    if current_status != temps_actuel() : current_status = temps_actuel()

    # On met à jour le temps actuel dans le champs text du Widget LABEL pour afficher l'heure
    status_temps_actuel["text"] = temps_actuel()

    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_temps_actuel)
    
#------------------------------------------------------------------------------
