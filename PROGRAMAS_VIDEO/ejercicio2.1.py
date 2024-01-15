class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print( "el animal esta volando")

class Mamifero(Animal):
    def amamantar(self):
        print( "el animal esta amamantando")

class Murcielago(Mamifero, Ave):
    pass

ave = Ave()

ave.comer()
ave.volar()

print (Murcielago.mro())


