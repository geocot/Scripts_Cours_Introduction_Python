#Pair et impair

liste = [1,2,3,4,5,6]
listePair = []
listeImpair= []

for nb in liste:
    if nb%2 == 0:
        listePair.append(nb)
    else:
        listeImpair.append(nb)

print('Pair {} et impair {}'.format(listePair,listeImpair))