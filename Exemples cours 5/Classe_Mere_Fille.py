class Mere:
    def bonjour(self):
        return "Vous avez le bonjour de la classe mère !"


class Fille(Mere):
    def salut(self):
        return "Un salut de la classe fille !"


if __name__ == "__main__":
    fille = Fille()
    print(fille.salut())
    print(fille.bonjour())

