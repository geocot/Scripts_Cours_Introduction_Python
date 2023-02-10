import time
sudoku =   [[0, 0, 8, 0, 2, 0, 0, 0, 9],
            [0, 0, 7, 0, 0, 0, 4, 0, 2],
            [2, 0, 0, 7, 9, 0, 0, 1, 0],
            [0, 0, 9, 0, 0, 5, 3, 0, 6],
            [0, 6, 0, 0, 4, 0, 8, 9, 0],
            [7, 0, 4, 9, 0, 0, 1, 0, 0],
            [0, 7, 0, 0, 3, 6, 0, 0, 1],
            [5, 0, 3, 0, 0, 0, 7, 0, 0],
            [6, 0, 0, 0, 5, 0, 2, 8, 0]]

#Vérifie si la valeur peut y être placée
def testValeur(sudoku, i, j, v):
  if testLigne(sudoku,i,v):
    if testColonne(sudoku,j,v):
      #Vérifie si la valeur se retrouve dans le bloc 3x3
      ligneBlocTop, colonneTopBloc = 3 * (i // 3), 3 * (j // 3) #Trouve la partie haut/gauche du bloc.
      for x in range(ligneBlocTop, ligneBlocTop + 3):
          for y in range(colonneTopBloc, colonneTopBloc + 3):
              if sudoku[x][y] == v:
                  return False
      return True


#Vérifie si la valeur se retrouve dans la ligne
def testLigne(sudoku, iLigne, valeur):
    for i in range(9):
        if sudoku[iLigne][i] == valeur:
            return False
    return True

#Vérifie si la valeur se retrouve dans la colonne
def testColonne(sudoku, iColonne, valeur):
    for i in range(9):
        if sudoku[i][iColonne] == valeur:
            return False
    return True


def parcourGrille(grille):
    ligne = 0
    colonne = 0
    compteurCaseNon0 = 0
    compteurCaseNonChangee = 0
    listeValeursValides = []
    rechercher = True
    tempsDepart = time.time()
    while rechercher:
        if grille[ligne][colonne] == 0:
            compteurCaseNon0 = 0
            #Essai les valeurs de 0 à 9
            for valeur in range(0, 10):
                if testValeur(grille, ligne, colonne, valeur):
                    listeValeursValides.append(valeur)
            if len(listeValeursValides) == 1:
                compteurCaseNonChangee = 0
                grille[ligne][colonne] = listeValeursValides[0]  # Modification de la valeur de la grille
            listeValeursValides.clear()
        compteurCaseNonChangee+=1
        compteurCaseNon0+=1
        colonne+=1
        if colonne ==9:
            ligne+=1
            colonne=0
        if ligne==9:
            ligne=0
        #Conditions pour l'arrêt de la recherche
        if compteurCaseNon0>81:
            rechercher=False
            print("Voici la solution")
        if compteurCaseNonChange >162:
            rechercher=False
            print("Impossible à trouver, voici où je ne peux plus avancer")
    tempsFin = time.time()
    for ligne in grille: #Affiche la solution
        print(ligne)
    print("En {} seconde".format(round((tempsFin-tempsDepart), 5)))


parcourGrille(sudoku)






