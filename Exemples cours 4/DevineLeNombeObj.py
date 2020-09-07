from tkinter import *
import random

class app:
    def __init__(self):
        self.fen = Tk()

        self.fen.title("Devine le nombre")
        self.fen.geometry("480x100")
        self.fen.resizable(0, 0)
        self.prenomTxt = StringVar()
        self.nombreUsagerTxt = StringVar()
        self.afficheUsagerTxt = StringVar(value="Devine le nombre entre 0 et 100")
        self.afficheUsager = Label(self.fen, textvariable=self.afficheUsagerTxt).place(relx=0.4, rely=0.20, anchor='center')

        self.nombreUsagerLabel = Label(self.fen, text="Entrer un nombre").place(x=0.0, y=30.0, anchor='nw')
        self.nombreUsagerEntry = Entry(self.fen, textvariable=self.nombreUsagerTxt).place(x=120.0, y=30.0, anchor='nw')
        self.boutTester = Button(self.fen, text="Tester", command=self._tester).place(x=300.0, y=30.0, anchor='nw')
        self.boutNouvellePartie = Button(self.fen,text="Nouvelle partie", command=self._nouvellePartie).place(x=130.0, y=55.0, anchor='nw')

        self.boutQuit = Button(self.fen, text="Fermer", command=self.fen.destroy).place(x=475,y=95, anchor='se')


        self.nombreAleatoire = -1
        self._nouvellePartie()
        self.fen.mainloop()


    def _nouvellePartie(self):
        self.nombreAleatoire = random.randint(0,100)
        self.afficheUsagerTxt.set("J'ai trouvé mon nombre")

    def _tester(self):
        intValeur = int(self.nombreUsagerTxt.get())
        if intValeur>self.nombreAleatoire:
            self.afficheUsagerTxt.set("Trop grand!")
        elif intValeur < self.nombreAleatoire:
            self.afficheUsagerTxt.set("Trop petit!")
        else:
            self.afficheUsagerTxt.set("GAGNÉ!")
app()