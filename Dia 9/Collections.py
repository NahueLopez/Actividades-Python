"""
Una Forma de utilizar varias librerias, en este caso utilizamos el counter

"""
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

#Para saber que cantidad de numeros se repiten
numeros =[8,6,9,5,4,5,5,5,8,7,4,5,4,6,2,4,7]
print(Counter(numeros))
#Sabemos la cantidad de veces que se repite cada letra
print(Counter("ajsduioqhweasdqwe"))
#Sabemos la cantidad de palabras que se repiten, el split es para ver los espacios
frase = "al pan pan y al vino vino"
print(Counter(frase.split()))
#El most_common nos ordena que numero se ve mas veces, si ponemos en el ultimo () sabremos un numero especifico
serie = Counter([1,1,1,1,1,1,2,2,2,3,3,3,3,3,4])
print(serie.most_common())
print(list(serie))
#Diccionario por defecto, de esta forma si tenemos un error porque algo no existe
mi_dic = {'uno':"verde",'dos':"azul","tres":"rojo"}
print(mi_dic["dos"])
#De esta manera si buscamos otro resultado en el dic que no esta muestra nada
mi_dic1 = defaultdict(lambda :"nada")
mi_dic1["uno"] = "verde"
print(mi_dic1["dos"])
print(mi_dic1)
#Para tupla comun
mi_tupla = (500,18,65)
print(mi_tupla[1])
#De esta manera podemos acceder al dato de desde el nombre y por indice
#Se crea un objeto Persona y se le asigna a ariel
Persona = namedtuple("Persona",["nombre","altura","peso"])
ariel = Persona("Ariel",176,79)

print(ariel.altura)