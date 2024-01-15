from abc import ABC, abstractclassmethod

class Trbajador(ABC):

    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):

    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):

    @abstractclassmethod
    def dormir(self):
        pass


class Humano(Trbajador, Durmiente, Comedor):
    def comer(self):
        print("el humando esta comiendo")

    def trabajar(self):
        print("el humano esta trabajando")
    
    def dormir(self):
        print("el humano esta durmiendo")


class Robot(Trbajador):

    def trabajar(self):
        print("el robot esta trabajando")

robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
  
