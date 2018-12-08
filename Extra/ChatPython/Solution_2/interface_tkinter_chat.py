#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#AIDES: https://stackoverflow.com/questions/42062391/how-to-create-a-chat-window-with-tkinter

from Tkinter import *

fenetre = Tk()                      #Fenetre Principale declarer

def ChatRoom():
    global chat
    ChatFenetre = Toplevel()        #Sous-Fenetre ChatFenetre declarer
    
    messages = Text(ChatFenetre)    #Utilisation d'un Widget Text
    messages.pack()                 #Insertion dans l'espace du Widget Text

    input_user = StringVar()                            #Variable de Controle  cette variable speciale permet l'echange d'une valeur parmis plusieurs widget en direct en meme temps
    input_field = Entry(ChatFenetre, text=input_user)   #Widget Entry() est un widget de champ d'entré (FENETRE,text=CONTENUE) // Le Message de l'utilisateur sera saisi ICI meme
    input_field.pack(side=BOTTOM, fill=X)               #Insertion dans l'espace du Widget Entry

    def Enter_pressed(event):
        input_get = input_field.get()                   #Pour récupérer le texte de l'entrée actuelle, on utilise la méthode get
        print(input_get)                                #Affichage du Message saisi par l'utilisateur dans la console
        messages.insert(INSERT, '%s\n' % input_get)     #Affichage du Message dans le Widget TEXT
        # label = Label(window, text=input_get)
        input_user.set('')
        # label.pack()
        return "break"

    frame = Frame(ChatFenetre)  # , width=300, height=300)  #Ajout d'une Frame
    input_field.bind("<Return>", Enter_pressed)             #Lorsque le Bouton Entree est pressee alors , la fonctionnalitee Enter_pressed(event) commencera
    frame.pack()                                            #Insertion du Widget Frame dans l'espace allouable


Button(fenetre, text="Go a la ChatRoom", command=ChatRoom).pack()   #Bouton d'acces au Chat dans le menu principale
Button(fenetre, text="Fermer...", command=fenetre.quit).pack()      #Bouton de Fermeture du Programme
#window.mainloop()
fenetre.mainloop()    
