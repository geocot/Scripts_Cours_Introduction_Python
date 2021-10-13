from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass

class carre(Forme):
    def __init__(self, largeur,longueur):
        self._largeur = largeur
        self._longueur = longueur

    def aire(self):
        return self._longueur*self._largeur
    def perimetre(self):
        return 2*(self._longueur) + 2*(self._largeur)

c = carre(10,10)

print(c.aire())
