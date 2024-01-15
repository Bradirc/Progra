# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar palabra
#         pass

# class CorrectorOrtgrafico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self,texto):
#         #usamos el dicionario para corregir el texto
#         pass


from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar que la palabra esta en el diccionario
        pass


class CorrectorOrtgrafico:
    def __init__(self, verificador):
        self.verificador = verificador


corrector = CorrectorOrtgrafico(Servicioweb())