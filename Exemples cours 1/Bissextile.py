#Réponse à l'exercice 2.2
# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non

annee = input("Entrer une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

bissextile = False # On crée un booléen qui vaut faux

if annee % 4 != 0:
    bissextile = False
elif annee % 4 ==0:
    if annee % 100 != 0:
        bissextile = True
    elif annee %100 ==0:
        if annee % 400 != 0:
            bissextile = False
        else:
            bissextile = True

if bissextile:
    print("L'année entrée est bissextile")
else:
    print("L'année entrée n'est pas bissextile")


