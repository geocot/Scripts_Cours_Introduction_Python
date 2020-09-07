class Point:
    "Classe Point géographique contenant une position"
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def setx(self, x):
        self._x = x
    def sety(self, y):
        self._y = y
    def __str__(self):
        return 'Coord X = {}, Coord Y = {}'.format(self._x, self._y)
class Rectangle:
    "Classe Rectangle contenant une position"
    def __init__(self,largeur, hauteur, origine):
        self._largeur=largeur
        self._hauteur=hauteur
        self._origine = origine
    def getLargeur(self):
        return self._x
    def getHauteur(self):
        return self._y
    def setLargeur(self, x):
        self._x = x
    def setHauteur(self, y):
        self._y = y
    def setOrigine(self, origine):
        self._origine =origine
    def getOrigine(self):
        return self._origine
    def __str__(self):
        return "La largeur est {}, la hauteur est {} et l'origine est : {}".format(self._largeur, self._hauteur, self._origine)

if __name__ == "__main__":
    p1 = Point(1,1)
    r1 = Rectangle(10,20,p1)

    print(r1.__str__())

