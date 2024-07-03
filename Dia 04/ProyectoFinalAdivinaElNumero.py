#Ejercicio final adivina el numero
from random import *


nombre = input("Buenas! puedes indicarme tu nombre? \n")

print(f"Bueno {nombre} he pensado un numero entre el 1 y el 100 tienes solamente 8 intentos para adivinarlo\n")
print("¡Vamos que comience el juego!\n")

intentos = 0
exito = randint(1,100)

while intentos != 8:
    numero = int(input("Cual es el numero\n"))
    intentos += 1
    if ((numero < 0) or (numero > 100)):
        print(f"Selecciona un numero entre el 1 y 100, el {numero} no es valido")
    elif numero < exito:
        print(f"El numero: {numero} es menor al numero que elegi")
    elif numero > exito:
        print(f"El numero:{numero} es mayor al numero que elegi")
    else:
        print(f"FELICIDADES GANASTE, el numero que pense es {exito}")
        print(f"Te costo {intentos} intentos")
else:
    print("Se pasaron los 8 intentos, lo siento vuelve a intentarlo!")


