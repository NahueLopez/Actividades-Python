#Forma larga
"""
palabra = "python"

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

lista = [letra for letra in palabra] #Forma reducida, del ejemplo de arriba
print(lista)

lista = [n for n in range(0,20,2)]
print(lista)

lista = [n/2 for n in range(0,20,2)]
print(lista)

lista = [n if n*2 > 10 else "no" for n in range(0,20,2) ] #En este caso, tenemos un if y un else dentro de un for
print(lista)
"""
#EJemplo
"""
pies = [10,20,30,40,50]
metros = [n*3.281 for n in pies] #Lo que hacemos es multiplicamos*3.281 cada dato de la lista pies y la guardamos en la nueva
print(metros)
"""
#Ejemplo 1
"""
valores = [1, 2, 3, 4, 5, 6, 9.5]
print(valores)
valores_pares = [v for v in valores if v%2 == 0] #En este caso como no colocamos else, va leugo del for
print(valores_pares)
"""

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(g-32)*(5/9) for g in temperatura_fahrenheit ]