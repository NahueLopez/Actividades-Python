#1
"""
#Una funcion que arroje dos dados al azar
#La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
#Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
from random import *

def lanzar_dados():
    dado1= randint(1,6)
    dado2 = randint(1,6)
    return (dado1,dado2)

def evaluar_jugada (dado1,dado2):
    suma_dados = dado1 + dado2
    resultado = ""
    if suma_dados <= 6:
        resultado= (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 6 < suma_dados < 10:
        resultado = (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        resultado = (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

    return (resultado)

dado1,dado2 = lanzar_dados()
print(evaluar_jugada(dado1,dado2))
"""
#2
"""
#Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros),
#y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando
#el valor más alto. El orden de los elementos puede modificarse.
#Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
#Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y
#que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

    lista_numeros = [1,2,15,7,2]

    def reducir_lista(lista_numeros):
        lista = set(lista_numeros)
        lista =  lista.union(set(lista_numeros))
        lista= list(lista)
        lista.pop(-1)
        return(lista)


    def promedio(lista):
        suma = 0
        cont = 0

        for l in lista:
            suma += l
            cont += 1

        resultado =suma/cont
        return(resultado)

lista= reducir_lista(lista_numeros)
print(promedio(lista))
"""
#3
#Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe
#poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
#Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del
#lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores
#y llamarla lista_numeros).
#Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla
#(devolverla como lista vacía []).
#Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

from random import *
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def lanzar_moneda():
    moneda = ["Cara","Cruz"]
    aleatorio = choice(moneda)
    return aleatorio

def probar_suerte(aleatorio,lista_numeros):

    if aleatorio == "Cara":
        lista_numeros.clear()
        print(f"La lista se autodestruirá {lista_numeros}")
        return (lista_numeros)
    else:
        print(f"La lista fue salvada {lista_numeros}")
        return (lista_numeros)
    """
    match aleatorio:
        case "Cara":
            lista_numeros.clear() #Sirve para eliminar todos los elementos de una lista
            print(f"La lista se autodestruirá {lista_numeros}")
        case "Cruz":
            print(f"La lista fue salvada {lista_numeros}")
    """
aleatorio = lanzar_moneda()
probar_suerte(aleatorio,lista_numeros)