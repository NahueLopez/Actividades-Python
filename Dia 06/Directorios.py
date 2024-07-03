import os
"""
#ruta = os.getcwd()#Nos muestra en donde estamos
#ruta = os.chdir("C:\\Users\\Nahue\\Desktop\\Estudios\\Analista\\") #De esta manera nos transladamos a otra ruta para acceder a los archivos
#ruta = os.makedirs("C:\\Users\\Nahue\\Desktop\\Estudios\\Analista\\Otra") #De esta manera creamos una carpeta en otro lugar
ruta = "C:\\Users\\Nahue\\Desktop\\Estudios\\Analista\\MATEMATICA.txt"
#elemento = os.path.basename(ruta)#Traemos el elemento base
#elemento = os.path.dirname(ruta)#Traemos la priemra parte la ruta
#elemento = os.path.split(ruta)#Nos trae una tupla la cual nos diferencia la primera parte de la ruta, y luego el elemento base

print(elemento)

"""
#Para eliminar un directorio

#os.rmdir("C:\\Users\\Nahue\\Desktop\\Estudios\\Analista\\Otra")

#Es una forma de traer archivos, pero tendremos problemas en diferentes Sistemas Operativos
"""
otro_archivo =  open("C:\\Users\\Nahue\\Desktop\\Estudios\\Analista\\MATEMATICA.txt")
print(otro_archivo.read())
"""
#Para trabaajr con un objeto en rutas
from pathlib import Path

#Forma larga
carpeta = Path("C:/Users/Nahue/Desktop/Estudios/Analista/") #Nos permite que podamos trabajar en diferentes Sistemas Operativos
archivo = carpeta / "MATEMATICA.txt"
miArchivo  = open(archivo)
#Forma corta
carpeta = Path("C:/Users/Nahue/Desktop/Estudios/Analista/") / "MATEMATICA.txt"
miArchivo  = open(carpeta)
print(miArchivo.read())