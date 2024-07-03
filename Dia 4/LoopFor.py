#Aplicaremos el for
#Mostraremos el numero de indice +1 y luego la letra que ocupa el lugar
"""
lista = ["a","b","c","d"]

for letra in lista:
    numeroLetra = lista.index(letra) + 1
    print(f"Letra: {numeroLetra}: {letra}")

"""
#En este caso buscamos en la lista y mostramos aquellos nombres que comienzan con L
"""
lista = ["Pablo","Laura","Fede","Luis","Julia"]

for nombre in lista:
    if nombre.startswith("L"):
        print(f"Los nombres que comienzan con L son: {nombre}")
    else:
        print(f"Nombre que no comienza con L son: {nombre}")
"""
#En este ejemplo mostramos como pasar el valor y sumarlo
"""
numeros = [1,2,3,4,5]
mivalor = 0

for numero in numeros:
    mivalor = mivalor + numero
    print(f"El valor es {mivalor}")
print(f"El valor es {mivalor}")
"""
#En este vemos como recorremos un string mostrando cada palabra
"""
palabra = "python es genial"

for letra in palabra:
    print(letra)
"""
#En este vemos que puedo colocar el elemento directametne
"""
for letra in "python es genial":
    print(letra)
"""
#En este vemos como recorremos una lista, que tiene mas listas en su interior
"""
palabra = [["a","b"],["c","d"],["e","f"]]

for letra in palabra:
    print(letra)
"""
#En este vemos como recorremos una lista, que tiene mas listas en su interior y asignamos mas de una variable
"""
palabra = [["a","b"],["c","d"],["e","f"]]

for a,b in palabra:
    print(a) #Podemos solo mostrar una sola variable
    print(b)
"""
#En este vemos como recorremos un diccionario
"""
dic = {"clave1":"a","clave2":"b","clave3":"c"}

for a,b in dic.items(): #Podemos ver ya sea todo lo que tiene con .items-la clave sola.keys o .values para ver el valor
    print(a,b) #Podemos solo mostrar una sola variable
for items in dic.items():
    print(items)
"""
#Ejercicio prueba
"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares =  + numero
    else:
        suma_impares = suma_impares + numero

print(suma_pares)
print(suma_impares)
"""
#Palabras claves que usamos en for y while
#pass
"""
respuesta = "s"

while respuesta == "s":
    pass #Sirve para poder seguir sin terminar el while

print("Hola")
"""
#El break sirve para finalizar cuando se alcanza, en este caso al encontrar la letra r se finalizara el for
"""
nombre = input("Tu numebre: \n")

for letra in nombre:
    if letra == "r":
        break
    print(letra)
"""
#El continue sirve para hacer un salto cuando se encuentra esa letra, en este caso al encontrar la r saltara esa letra y seguira.
"""
nombre = input("Tu numebre: \n")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
"""