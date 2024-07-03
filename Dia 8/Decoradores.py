#Son funciones que modifican el comportamiento de otras funciones
#Las funciones en python son objetos

def cambiar_letras(tipo):



    def mayuscula(texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


"""Se puede asignar a una variable una funcion
mi_funcion = mayuscula

mi_funcion("python")"""

"""" Se le puede pasar una funcion a otra funcion
def una_funcion(funcion):
    return  funcion

una_funcion(mayuscula("probando"))"""

operacion = cambiar_letras("may")

operacion("palabra")