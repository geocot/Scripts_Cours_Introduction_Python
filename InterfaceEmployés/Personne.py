class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    @property
    def nom(self):
        return self._nom

    @property
    def prenom(self):
        return self._prenom
