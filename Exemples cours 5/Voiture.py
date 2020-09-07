class Voiture:
    "Classe voiture"
    def __init__(self, couleur, marque):
        self._couleur = couleur
        self._marque = marque
    def getCouleur(self):
        return self._couleur
    def setCouleur(self, couleur):
        self._couleur = couleur
    def __str__(self):
        return "{} et la marque est {}".format(self._couleur, self._marque)

class Couleur:
    def __init__(self, nomCouleur):
        self._nomCouleur = nomCouleur
    def getCouleur(self):
        return self._nomCouleur
    def setCouleur(self, nomCouleur):
        self._nomCouleur = nomCouleur
    def __str__(self):
        return "La couleur est {}".format(self._nomCouleur)
    

Rouge = Couleur("Rouge")
Bleu = Couleur("Bleu")

v1 = Voiture(Rouge,"Honda")
v2 = Voiture(Bleu,"Toyota")

listeVoiture = [v1,v2]
print(listeVoiture[0])