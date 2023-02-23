#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:27:07 2022

@author: lindsay
"""
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.probability import FreqDist
import pandas as pd
import mysql.connector
import shutil
#from config import *
mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="taln")
mycursor = mysqldb.cursor()
import os
main_path=os.getcwd()
def import_text(titre,text):
    main_path=os.getcwd()
    if not os.path.isdir(main_path+'/corpora'):
        os.mkdir(main_path+'/corpora')
    mycursor.execute('SELECT count(*) FROM `corpus`;')
    nb=mycursor.fetchone()
    name_file=f'corpus_{nb[0]+1}.txt'
    new_text=open(main_path+'/corpora/'+name_file,'w')
    new_text.write(text)
    file_path=main_path+'/corpora/'+name_file
    print('nombre :',name_file)
    print(("INSERT INTO `corpus`(`titre`, `filename`, `path`) VALUES ('{}','{}','{}')".format(titre,name_file,file_path)))
    mycursor.execute("INSERT INTO `corpus`(`titre`, `filename`, `path`) VALUES ('{}','{}','{}')".format(titre,name_file,file_path))
    mysqldb.commit()
    

import tkinter as tk

def message(text):
    global value
    # Créer la fenêtre principale
    window = tk.Tk()
    window.title("Fampitandremana")

    # Définir la taille de la fenêtre
    window.geometry("300x150")

    # Centrer la fenêtre sur l'écran
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculer les décalages x et y pour centrer la fenêtre
    x_offset = (screen_width - 300) // 2
    y_offset = (screen_height - 150) // 2

    # Définir les décalages x et y de la fenêtre
    window.geometry(f"+{x_offset}+{y_offset}")

    # Créer le texte
    text = tk.Label(window, text=f"{text}")
    text.pack()

    # Créer les boutons
    button1 = tk.Button(window, text="Eny")
    button2 = tk.Button(window, text="Tsia")
    button3 = tk.Button(window, text="Hiverina")

    # Placer les boutons horizontalement
    button1.place(x=10, y=80)  # Ajouter une marge en haut des boutons
    button2.place(x=110, y=80)
    button3.place(x=200, y=80)
 # Déclarez la variable value comme une variable de chaîne Tkinter

    # Définir les fonctions à exécuter lorsque les boutons sont cliqués
    def set_value1():
        global value
        # Mettre à jour la valeur de la variable value
        value="Eny"  # Utilisez la méthode set() de Tkinter pour mettre à jour la valeur de value
        window.destroy()
        return value
    def set_value2():
        global value
        # Mettre à jour la valeur de la variable value
        value="Tsia"
        window.destroy()
        return value

    def set_value3():
        global value
        # Mettre à jour la valeur de la variable value
        value="Hiverina"
        window.destroy()
        return value

    # Assigner les fonctions aux boutons
    button1.config(command=set_value1)
    button2.config(command=set_value2)
    button3.config(command=set_value3)

    # Afficher la fenêtre
    window.mainloop()
    response = value
    print(f'response={response}')
    return 

# Run the messagebox function


def show_text():
    global listbox,text_saisi

def statistics(text):
    # Tokenisation du texte
    tokens = nltk.wordpunct_tokenize(text)
    print(tokens)
    
    # Construction de la statistique des mots
    fdist = FreqDist(tokens)
    
    # Affichage des 10 mots les plus fréquents
    print(fdist.most_common(10))
    
    # Affichage de la fréquence du mot "text"
    print(fdist["text"])
    
    # Affichage de la longueur du vocabulaire (nombre de mots uniques)
    print(len(fdist))


def delete_session():
    session_path=main_path+r'/Session/'
    for filename in os.listdir(session_path):
        print(f'SESSION CACHE:{filename}')
        file_path = os.path.join(session_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Impossible de supprimer la session %s. Reason: %s' % (file_path, e))
def is_folder_empty(folder_path):
    return len(os.listdir(folder_path)) == 0
