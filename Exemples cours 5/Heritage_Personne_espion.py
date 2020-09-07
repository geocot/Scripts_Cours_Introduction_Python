class Personne:
    "Classe personne"

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def __str__(self):
        return 'Mon prenom est {} et mon nom est {}'.format(self._prenom, self._nom)


class Espion(Personne):
    "Espion"
    def __init__(self, nom, prenom, nomCode):
        Personne.__init__(self,nom, prenom)
        self._nomCode = nomCode
    def getNom(self):
        return self._nom
    def setNom(self, nom):
        self._nom = nom
    def __str__(self):
        return 'Mon prenom est {} et mon nom est {}, code {}'.format(self._prenom, self._nom, self._nomCode)


e = Espion("Bond", "James","007")
print(e)
print(e.getNom())
e.setNom('Bonde')
print(e)