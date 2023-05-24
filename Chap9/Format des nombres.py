#Pour insérer un espace pour aligner les nombres positifs et négatifs
print("-5")
print("{: }".format(5))

#Formatage en binaire
print("Le nombre {0} en binaire est {0:b}".format(6))
#Le nombre 6 en binaire est 110

#Pour changer en valeur entière
txt = "Il y a {:d} planètes."
print(txt.format(0b1000))

#Pour utiliser les exposants
txt = "Nous avons {:e} poules."
print(txt.format(500000))
#Nous avons 5.000000e+05 poules.

#Pour limiter les décimaux
#Par défaut, c'est 6 décimales
txt = "Le prix est de {:f} dollars."
print(txt.format(45))
#Le prix est de 45.000000 dollars.

#Pour les hexadécimaux
txt = "La valeur hexadecimal de {0} est {0:x}"
print(txt.format(255))
#La valeur hexadecimal de 255 est ff

#Pour l'utilisation du pourcentage
txt = "Votre note est {:%}"
print(txt.format(0.75))
#Votre note est 75.000000%

#Sans décimaux
txt = "Votre note est {:.0%}"
print(txt.format(0.75))
#Votre note est 75%


