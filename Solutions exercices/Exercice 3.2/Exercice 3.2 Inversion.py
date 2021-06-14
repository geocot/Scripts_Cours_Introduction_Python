# Lire la variable string s
s = input("Tapez une chaine : ")
# initialiser l'inverse à une chaine vide
inv = ""

# construction de l'inverse d'une façon récursive
for x in s:
    inv = x + inv
print("L'inverse de la chaine : '",s,"' est : ", inv)
#Les virgules dans le print permet d'afficher plusieurs variables sur une même ligne.