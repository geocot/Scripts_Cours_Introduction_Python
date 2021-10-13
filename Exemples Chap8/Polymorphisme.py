"""
En Python, le polymorphisme nous permet de définir des méthodes
dans la classe enfant portant le même nom que les méthodes de la classe mère.
"""

class Personne:
    def __init__(self, nom):
        self.nom = nom

    def affiche(self):
        print("je suis une personne")


class Etudiant(Personne):
    def __init__(self, nom, cne):
        super().__init__(nom)
        self.cne = cne

    def affiche(self):
        print("je suis un etudiant")

