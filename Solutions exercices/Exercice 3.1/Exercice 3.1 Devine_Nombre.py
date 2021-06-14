import random
nombreAletatoire = random.randint(0,100)
#Source: https://docs.python.org/2/library/random.html

gagne = False
nbCoup = 0
while gagne == False:
    nbCoup+=1
    valUsager = input('Entrer une valeur entre 0 et 100: ')
    if int(valUsager) == nombreAletatoire:
        gagne = True
        print('Bravo, vous avez trouvé!', 'Nombre de coups:',nbCoup)
    elif int(valUsager)< nombreAletatoire:
        print("Trop bas!")
    else:
        print("Trop haut!")
