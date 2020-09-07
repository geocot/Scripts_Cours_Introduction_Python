class Personne:
    "Personne"
    nbClasse = 0
    def __init__(self, nom):
        self._nom = nom
        Personne.nbClasse +=1

    def nbClassePersonne(cls):
        print("Le nb de classes est {}".format(cls.nbClasse))

p1 = Personne('Robert')
p1 = Personne('Rob')
p1.nbClassePersonne()


