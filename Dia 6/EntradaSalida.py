#Para leer un archivo
"""
miArchivo = open("prueba.txt")

print(miArchivo.read())

miArchivo.close()
"""

#Para leer una linea
"""
miArchivo = open("prueba.txt")

unaLinea = miArchivo.readline()
print(unaLinea.upper())#Lo que hace es hacer todo mayuscula igual que en un string ya que es igual a un string

unaLinea = miArchivo.readline()
print(unaLinea.rstrip()) #Esto es para sacar los espacios de linea que se crean

unaLinea = miArchivo.readline()
print(unaLinea) #Esto lo que hace es leer una linea y otra, es porque luego de que lea la primera linea y genera un punto y luego sigue en la proxima

miArchivo.close()
"""

#Con un loop
"""
miArchivo = open("prueba.txt")

for l in miArchivo: #Va leyendo por lineas
    print("Aqui dice: " + l)

miArchivo.close()
"""

#Readlines en plural
"""
miArchivo = open("prueba.txt")

todas = miArchivo.readlines()#Crea una lista con todas las lineas
#ejemplo
todas = todas.pop()#Guardamos el ultimo elemento

print(todas)

miArchivo.close()
"""

