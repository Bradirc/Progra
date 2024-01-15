def decorador(funcion):
    def funcion_modificada():
        print("Antes de llmar la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("hola brandon como andas")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola brandon como andas")

saludo()