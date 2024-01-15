class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"

    def _hablar(self):
        print("hola, como estas")

objeto = MiClase()
print(objeto._hablar())