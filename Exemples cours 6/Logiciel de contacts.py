# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:24:02 2018

@author: Martin
"""
import pickle
from tkinter import *
from tkinter import filedialog

class monApp:
    def __init__(self):
        self.fen = Tk()
        
        self.positionListe =0
        self.ListeDePersonnes = []
        self.prenomTxt = StringVar()
        self.nomTxt = StringVar()

        self.fen.title("Contacts")
        self.label = Label(self.fen, text="Entrer les information").grid(row=0)
        self.boutQuit = Button(self.fen, text="Fermer", command=self.fen.destroy).grid(row=5, column=3)
        self.btnSauv = Button(self.fen, text="Sauvegarder", command=self.sauvegarder).grid(row=4, column=2)
        self.btnCharge = Button(self.fen, text="Charger", command=self.charger).grid(row=4, column=1)
        self.btnNouv = Button(self.fen, text="Nouvelle", command=self.nouvellePersonne).grid(row=3, column=0)
        self.btnSuivant = Button(self.fen, text=">", command=self.suivant).grid(row=3, column=1, sticky="e")
        self.btnPrecedent =Button(self.fen, text="<", command=self.precedent).grid(row=3, column=1, sticky="w")
        self.nomLabel = Label(self.fen, text="Nom:").grid(row=1, column=0)
        self.nomEntry = Entry(self.fen, textvariable=self.nomTxt).grid(row=1, column=1)
        self.prenomEntry = Entry(self.fen, textvariable=self.prenomTxt).grid(row=2, column=1)
        self.prenomLabel = Label(self.fen, text="Prénom:").grid(row=2, column=0)
        self.fen.title("Contacts ({})".format(len(self.ListeDePersonnes)))
        self.fen.mainloop()
        
    def sauvegarder(self):
        filename = filedialog.asksaveasfilename(title="Ouvrir votre document",filetypes=[('pkl files','.pkl'),('all files','.*')])
        fichier = open(filename, "wb")
        pickle.dump(self.ListeDePersonnes, fichier)
        fichier.close()

    def charger(self):
        filename = filedialog.askopenfilename(title="Ouvrir votre document",filetypes=[('pkl files','.pkl'),('all files','.*')])
        fichier = open(filename, "rb")
        self.ListeDePersonnes = pickle.load(fichier)
        fichier.close()
        self.contactsUpdate()
       

    def nouvellePersonne(self):
        self.ListeDePersonnes.append(personne(self.prenomTxt.get(), self.nomTxt.get()))
        self.prenomTxt.set("")
        self.nomTxt.set("")
        self.contactsUpdate()

      
    def suivant(self):
        #print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe +=1
        
        if self.positionListe == len(self.ListeDePersonnes):
            self.positionListe = 0
        self.contactsUpdate()

    def precedent(self):
        print(self.positionListe)
        self.prenomTxt.set(self.ListeDePersonnes[self.positionListe].prenom)
        self.nomTxt.set(self.ListeDePersonnes[self.positionListe].nom)
        self.positionListe -=1 
        print(self.positionListe)
        if self.positionListe < 0:
            self.positionListe = len(self.ListeDePersonnes)-1
        self.contactsUpdate()

    def contactsUpdate(self):
        self.fen.title("Contacts ({})".format(len(self.ListeDePersonnes)))   
        
class personne:
    "Objet qui représente une personne"
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

        
    def __str__(self):
        return "Le nom est {} {}".format(self.prenom, self.nom)
        



monApp()
