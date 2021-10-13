
class personne:
    def __init__(self,nom, prenom):
        self._nom = nom
        self._prenom = prenom
        
    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        self._nom = value


p1 = personne("Couture", "Martin")
print(p1.Nom)
p1.Nom = "Robert"
print(p1.Nom)


