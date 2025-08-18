#Martin Couture
#Permet de calculer l'aire d'un polygone. 
#Explication ici: https://youtu.be/IPrNwZFIT1o

#Suite de coordonnées
polygoneCarre=[(-7950100,5921400),(-7949040,5921400),(-7949040,5920550),(-7950100,5920550)]
polygoneIrr=[(-7949510.292,5919714.513),(-7948352.556,5920422.386), (-7947776.996,5919443.272),(-7949272.129,5919469.735)]
carre = [(10,10),(20,10),(20,5),(10,5)]
#Regroupement des latitudes et longitudes
def regroupement(polygone):
    x=[]
    y=[]
    for point in polygone:
        x.append(point[0])
        y.append(point[1])
    return x,y
#Multiplication des coordonnées
def lacet(listex, listey):
    A1 = 0
    A2 = 0

    for n in range(len(listex)):
        A1+=listex[n]*listey[(n+1) % (len(listex))]
    print("A1=", A1)
    for n in range(len(listex)):
        A2+=listey[n]*listex[(n+1) % (len(listex))]
    print("A2=", A2)

    return abs((A1-A2)/2)

listeXY=regroupement(polygoneIrr)
print("Aire = ", lacet(listeXY[0],listeXY[1]))

