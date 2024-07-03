#if, importante si no se tabula no funciona
"""
if (10 > 9) :
    print("Es correcto")
if (True) :
    print("Es correcto") #Si lo que ponemos es True o una variable con ese type, tomara como correcto
if (False) :
    print("Es correcto") #Si lo que ponemos es False o una variable con ese type, tomara como incorrecto
"""
#Con else, la forma correcta de tabular
"""
if (5 == 2):
    print("Es correcto")
else:
    print("Es incorrecto")
"""
#Ejemplo de como anidar if, elif
"""
mascota = "pez"

if (mascota == "gato"):
    print("Tienes un gato")
elif (mascota == "perro"):
    print("Tienes un perro")
elif (mascota == "pez"):
    print("Tienes un pez")
else:
    print("Nose que animal tienes")
"""
#Otro ejemplo
"""
edad = 16
calificacion = 9

if (edad < 18):
    print("Eres menor de edad")
    if (calificacion >= 7):
        print("Aprobaste")
    else:
        print("Desaprobaste")
else:
    print("Eres adulto")
"""
#Ejercicio de muestra
"""

#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

#"Cumples con los requisitos para postularte"

#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

#"Para postularte, necesitas tener conocimientos de inglés"

#"Para postularte, necesitas saber programar en Python"

#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

habla_ingles = True
sabe_python = False

if habla_ingles:
    if sabe_python:
        print("Cumples con los requisitos para postularte")
    else:
        print("Para postularte, necesitas saber programar en Python")

elif not habla_ingles:
    if not sabe_python:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    else:
        print("Para postularte, necesitas tener conocimientos de inglés")
"""