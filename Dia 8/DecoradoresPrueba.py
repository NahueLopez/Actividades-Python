def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion

#La forma de dedorar es crear las funcion y luego utilizar el @{nombre de la funcion}
#@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

#agrego el decorado en una variable y la uso si quiero o no
mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula("nahue")

mayuscula_decorada("nahue")