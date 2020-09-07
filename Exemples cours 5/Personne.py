class Personne:
    'Ceci fait une personne'
    def __init__(self, prenom, nom):
        self._nom = nom
        self._prenom = prenom
        self._carte = []
    def getPrenom(self):
        return self._prenom
    def setPrenom(self, prenom):
        if type(prenom) == str:
            self._prenom = prenom
    def getNom(self):
        return self._nom
    def setNom(self,nom):
        self._nom = nom
    def setCredit(self,credit):
        self._carte.append(credit)
    def getListeCredit(self):
        return self._carte
    def getNbCredit(self):
        return len(self._carte)
    def __str__(self):
        return "Le nom est {}, le prenom est {}".format(self._nom, self._prenom)

class CarteCredit:
    "Carte de crédit"
    def __init__(self, noCarte, Expiration):
            self._noCarte = noCarte
            self._expiration = Expiration
    def __str__(self):
        return "Le numéro est {} et l'expiration est {}".format(self._noCarte,self._expiration)

class Client(Personne):
    def __init__(self, prenom, nom, dateinscription, courriel):
        #Personne.__init__(self,prenom,nom)
        super().__init__(prenom,nom)
        self._dateinscription = dateinscription
        self._courriel = courriel

    def __str__(self):
        return "Prenom {}, nom {}, di {}, courriel {}".format(self._prenom, self._nom, self._dateinscription, self._courriel)



if __name__ == "__main__":
    c1 = CarteCredit('12456', "12/6")
    p1 = Personne('Martin', 'Couture')
    client1 = Client("Martin", "Coutu", "12/6", "aa@aa.ca")
    print(client1)


