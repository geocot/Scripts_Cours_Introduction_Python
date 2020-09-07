from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass
    def couleur(self):
        return "Rouge"


class rect(Forme):
    def __init__(self, largeur,longueur):
        self._largeur = largeur
        self._longueur = longueur
    def aire(self):
        return self._largeur* self._longueur
    def perimetre(self):
        return 2*self._longueur + 2*self._largeur

    def couleur(self):
        return "Blanc"

r = rect(10,10)
print(r.couleur())

class carre(Forme):
    def __init__(self, largeur,longueur):
        self._largeur = largeur
        self._longueur = longueur

    def aire(self):
        return self._longueur*self._largeur
    def perimetre(self):
        return 2*(self._longueur) + 2*(self._largeur)

c = carre(10,10)
print(c.couleur())
print(c.aire())
