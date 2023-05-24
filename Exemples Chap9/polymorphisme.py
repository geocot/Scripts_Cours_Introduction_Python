class Ours():
    def crie(self):
        print("Groarrr")
class Chien():
    def crie(self):
        print("Warf warf!")
def lanceCrie(animal):
    animal.crie()


oursObj = Ours()
chienObj = Chien()

lanceCrie(oursObj)
lanceCrie(chienObj)
