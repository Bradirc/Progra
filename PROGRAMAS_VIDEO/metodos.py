class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print (f'Estas haciendo un llamado de un:{self.modelo}')
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')    


celular1 = Celular("Samsung", "S23", "48MP" )
celular2 =  Celular("Apple", "Iphone 15 pro", "90MP")

celular1.cortar()


  