class Gato():
    def sonido(self):
        return "miau"

class Perro():
    def sonido(self):
        return "guau"
    
def hacer_sonido(animal1):
    print(animal1.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(perro)