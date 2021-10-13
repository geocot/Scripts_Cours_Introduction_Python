def exp2(nombre):
    return nombre**2


listeNombre = [1,2,3,4,5]
lstResultat = map(exp2, listeNombre)


for resultat in lstResultat:
    print(resultat)
