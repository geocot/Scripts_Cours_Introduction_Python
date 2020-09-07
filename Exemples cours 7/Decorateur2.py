connecte = True

def verifConnexion(function):
    def wrapper():
        if connecte == True:
            return function()
        else:
            print("Vous n'êtes pas connecté")
    return wrapper

@verifConnexion
def listeRepertoire():
    print("Voici la liste des répertoires...")

@verifConnexion
def envoyerMsg():
    print("Msg envoyé")


listeRepertoire()
envoyerMsg()
