
def exempleDecorateur(function):
    print("Exécution du décorateur")
    return function

@exempleDecorateur
def bonjour():
    print("Bonjour")

@exempleDecorateur()
def bonsoir():
    print("Bonsoir")

bonjour()
bonsoir()

