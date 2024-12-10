import Personne
class Employe(Personne.Personne):
    def __init__(self, nom, prenom, id, date):
        Personne.Personne.__init__(self,nom, prenom)
        self._id = id
        self._date = date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f"{self._nom}, {self._prenom},{self._id},{self._date}"

    def versListe(self):
        return [self.nom, self.prenom, self.id, self.date]