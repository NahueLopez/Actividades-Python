#Muestra de como funciona un while
"""
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    #monedas = monedas -1
    monedas -= 1
else:
    print("No tengo mas dinero")
"""
#Un ejemplo de uso de while
"""
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres Seguir (s/n) \n")
else:
    print("Gracias")
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
