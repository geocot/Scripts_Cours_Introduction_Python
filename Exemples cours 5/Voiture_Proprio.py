class Voiture():
    def __init__(self, couleur, modele, annee, proprio):
        self._couleur = couleur
        self._modele = modele
        self._annee = annee
        self._proprio = proprio

    def getCouleur(self):
        return self._couleur
    def getModele(self):
        return self._modele
    def getAnnee(self):
        return self._annee
    def getProprio(self):
        return self._proprio

    def setCouleur(self, value):
        self._couleur = value

    def setModel(self, value):
        self._modele = value

    def setAnnee(self, value):
        self._annee = value

    def setProprio(self, value):
        self._proprio = value

    def __str__(self):
        return "La couleur est {}, modele {}, année {} et le proprio : {}".format(self._couleur, self._modele, self._annee, self._proprio)

class Proprio():
    def __init__(self, prenom, nom):
        self._prenom = prenom
        self._nom = nom

    def getPrenom(self):
        return  self._prenom
    def getNom(self):
        return  self._nom

    def __str__(self):
        return "Le prénom est {} et le nom est {}".format(self._prenom, self._nom)

if __name__ == "__main__":
    p = Proprio("George", "Tremblay")
    v = Voiture("Rouge", "Cadillac", 1958, p)
    print(p)
    print(v)
