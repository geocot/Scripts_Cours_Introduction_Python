
def exempleDecorateur(function):
    print("Exécution du décorateur")
    return function


@exempleDecorateur
def bonjour():
    print("Bonjour")


bonjour()


