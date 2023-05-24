from string import Template

class monTemplate(Template):
    delimiter = "?"

def Main():
    panier = []
    panier.append(dict(item="Orange", prix=0.99, qty=100))
    panier.append(dict(item="Pomme", prix=0.79, qty=110))
    panier.append(dict(item="Banane", prix=0.39, qty=210))

    t=monTemplate("?qty x ?item = ?prix")
    total = 0
    print("Panier:")
    for element in panier:
        print(t.substitute(element))
        total +=element["prix"] * element["qty"]
    print("Total: " + str(total))

Main()

d = dict(nom='Popeye')
print(Template('$nom mange des épinards').substitute(d))
#Popeye mange des épinard

