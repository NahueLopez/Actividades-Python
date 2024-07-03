#El metodo random lo tenemos que traer desde una libreria, tener en cuenta de no crear un archivo con el mismo nombre de una libreria
from random import *
#Nos trae un numero aleatorio dentro del parametro que establecimos

aleatorio = randint(1,50)
print(aleatorio)
#Nos tre un numero aleatoreo dentro del parameto pero con coma
aleatorio = round(uniform(1,5),1)
print(aleatorio)
#Nos trae un numero aleatorio con coma entre 0 y 1
aleatorio = random()
print(aleatorio)
#Trae algo aleatorio de una lista
colores = ["azul","rojo","verde","violeta"]
aleatorio = choice(colores)
print(aleatorio)
#Esto sirve para mezclar
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)