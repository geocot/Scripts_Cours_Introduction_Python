class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
    def getNom(self):
        return self._nom
    def getPrenom(self):
        return self._prenom


#Sauvegarde
def sauvegarde(listePersonne):
    fichier = open(r"c:\temp\personnes.txt", 'w')
    for personne in listePersonne:
        fichier.write("{},{}\n".format(personne.getNom(), personne.getPrenom()))
    fichier.close()

#Récupération
def recuperation():
    listePersonne=[]
    fichier = open(r"c:\temp\personnes.txt", 'r')
    lp = fichier.readlines()
    for personne in lp:
        infos = personne.split(",")
        p = Personne(infos[0], infos[1])
        listePersonne.append(p)
    fichier.close()
    return listePersonne
    
p1 = Personne("Couture", "Martin")
lp = [p1]
sauvegarde(lp)
listeObjetsPersonnes = recuperation()
print(listeObjetsPersonnes[0].getNom())
