#Ejercicio 1
"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.

def devolver_distintos(num1,num2,num3):

    suma = num1 + num2 +num3
    numeros = [num1,num2,num3]

    if suma > 15:
        maxi = max(numeros)
        return (maxi)

    elif suma < 10:
        mini = min(numeros)
        return (mini)
    else:
        numeros.sort()
        return(numeros[1])

print(devolver_distintos(10,2,5))

"""

#Ejercicio 2
"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d'
,
'e'
,
'i'
,
'n'
,
'o'
,
'r'
,
't']

palabra = "entretenido"
def revision(palabra):
    lista = list(palabra)
    lista = set(lista)
    return lista

resultado = (revision(palabra))
resultado = list(resultado)
resultado.sort()
print(resultado)
"""

#Ejercicio 3
"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False

def boolean(*args):
    cont = 0
    n = ""
    for arg in args:

        if (n == arg) and (n == 0):
                return True
        n = arg

    if cont < 2:
        return False

print(boolean(5,6,1,0,0,9,3,5))
print(boolean(0,1,5,1,0,3,0,1,0))
"""

#Ejercicio 4
"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""
def contar_primos(num):
    primo = [2]
    cont = 3

    if num < 2:
        return(0)

    while cont <= num:
        for n in range(3,cont,2): #Vamos del 3 al cont, y saltamos de a 2 porque sabemos que los pares no son primos

            if (cont % n == 0):
                cont += 2
        else:
            primo.append(cont)#Agregamos un valor a la lista
            cont += 2
    print(primo)
    return(len(primo))#Contamos cuantos elementos tiene la lista


print(contar_primos(50))