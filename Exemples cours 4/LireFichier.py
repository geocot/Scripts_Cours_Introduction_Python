chemin = r'c:\temp\demo.txt'

fichier = open(chemin,'r')
ligne = fichier.readline()

while ligne:
    print(ligne, end='')
    ligne = fichier.readline()


fichier.close()