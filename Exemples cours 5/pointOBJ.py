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

    def translation(self,valeur):
        self._x +=valeur
        self._y +=valeur

p1 = Point(-73,45)
p1.translation(2)
print(p1.getx())
print(p1.gety())


