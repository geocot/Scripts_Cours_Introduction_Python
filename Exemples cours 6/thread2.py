import threading, time

def affiche(texte):
    i = 0
    while i<10:
        print(texte)
        time.sleep(0.3)
        i+=1

a = threading.Thread(target=affiche, args=("########",)) #La virgule est pour dire que c'est un tuple. Sinon il prend chaque caractère pour un arg.
b = threading.Thread(target=affiche, args=("00000000",))

a.start()
b.start()
a.join()
b.join()

print("Terminé")