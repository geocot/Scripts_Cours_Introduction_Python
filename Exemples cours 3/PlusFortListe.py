liste = [1,6,9,4,5,7]

plusFort = 0

for nb in liste:
    if nb>plusFort:
        plusFort = nb

print("Le plus fort de la liste est {}".format(plusFort))
