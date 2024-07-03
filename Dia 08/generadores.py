# Una funcion generadora lo que hace es te va creando los resultados no crearla completa sino de a paso para no generar
#problemas y cuida el espacio del ordenador, el generador recuerda donde quedo

#Una funcion que nos devuelva el numero 4
"""
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista


def mi_generador():
    for x in range(1,5):

        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()

#Van generando en base a lo que vamos pidiendo
print(next(g))
print(next(g))
print(next(g))
print(next(g))
"""

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()


print(next(g))
print(next(g))

#Puede haber en el medio funciones y todo que no afecta en nada
print("Hola mundo")


print(next(g))

"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

def mi_generador():
    num = 0
    yield num

    while True:
        num += 1
        yield num


generador = mi_generador()

print(next(generador))
"""

"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def mi_generador():
    
    num = 7
    
    while True:
        yield num
        num += 7
            
generador = mi_generador()
"""


def vidas():
    vidas = 4

    while True:

        vidas -= 1

        if vidas > 1:
            yield f"Te quedan {vidas} vidas"
        elif vidas == 1:
            yield f"Te queda {vidas} vida"
        elif vidas == 0:
            yield "Game Over"

"""
Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida


perder_vida = vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
"""