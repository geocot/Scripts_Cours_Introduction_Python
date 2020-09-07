# Détection et positionnement d'un clic de souris dans une fenêtre :
#Source: Apprendre à programmer Python 3 de G.Swinnen
from tkinter import *
def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
    ", Y =" + str(event.y))
fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()

