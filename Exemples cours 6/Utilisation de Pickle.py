import pickle

class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
    def getNom(self):
        return self._nom
    def getPrenom(self):
        return self._prenom
    def __str__(self):
        return "Le nom est {} et le prénom est {}".format(self._nom,self._prenom)

#Sauvegarde
def sauvegarde(listePersonne):
    fichier = open(r"c:\temp\personnes.pkl", 'wb')
    pickle.dump(listePersonne, fichier)
    fichier.close()

#Récupération
def recuperation():
    fichier = open(r"c:\temp\personnes.pkl", 'rb')
    listePersonne = pickle.load(fichier)
    return listePersonne

p1 = Personne("Couture", "Martin")
lp = [p1]
sauvegarde(lp)
listeObjetsPersonnes = recuperation()
print(listeObjetsPersonnes[0].getNom())
