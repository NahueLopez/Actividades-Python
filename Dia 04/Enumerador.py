#Esto es para saber en que indice esta cada item
"""
lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1
"""
#Con enumerate
"""
lista = ["a","b","c"]

for indice,item in enumerate(lista):
    print(indice,item)
"""
#Con un inter
"""
for indice,item in enumerate(range(0,55)):
    print(indice,item)
"""
#Fuera de un loop - pasarlo a tuple para tener indice y objeto

lista = ["a","b","c"]

miTuple = list(enumerate(lista))
print(miTuple)
#Para traer un elemeno de esto se peude hacer
print(miTuple[1][0]) #el primero es al indice y luego el 0 ese el elemento

#Ejercicio de mostrar solamente el indice de aquellos que comience su nombre con M

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

miTuple = list(enumerate(lista_nombres))
for indice,letra in miTuple:
    if letra[0] == "M":
        print(indice)
