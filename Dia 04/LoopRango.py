#Veremos como utilizar en range
"""
lista = [1,2,3,4]

for numero in lista:
    print(numero)
#Mejor manera de hacerlo es con rango, que nos permite no requerir una lista para utilizar el for:

for numero in range(5): #Recorrera del 0 al 4, el numero que pongamos no es inclusivo y comenzara del 0
    print(numero)

for numero in range(1,5): #Recorrera del 1 al 4, el numero que pongamos al final no es inclusivo,
    print(numero)

for numero in range(0,31,2): #Recorrera del 0 al 31, el numero que pongamos al final no es inclusivo, pero ira salteando de a 2
    print(numero)
"""
#Como utilizar un range para crear una lista
"""
lista = list(range(1,101)) #De esta manera lo que haremos es crear una lista del 1 al 100, sin necesidad de poner los numeros

print(lista)
"""
lista = list(range(1,16))
suma_cuadrados = 0
for suma in lista:
    suma = suma**2
    suma_cuadrados = suma_cuadrados + suma
