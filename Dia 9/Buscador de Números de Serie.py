import os
from datetime import datetime
from time import time
import re
import os.path
from math import ceil


def buscador (texto,arch):

    patron = 'N'+r'\D{3}'+'-'+r'\d{5}'
    buscador = re.search(patron,texto)


    if buscador:

        list.append(f"{arch}\t{buscador.group()}")


def fecha():

    fecha = datetime.today()
    fecha = fecha.strftime("%d/%m/%Y")
    return (f"Fecha de búsqueda: {fecha}" )


def recorrerCarpeta(ruta):

    for carpeta, subcarpeta, archivo in os.walk(ruta):

        for arch in archivo:
            abrir = open(os.path.join(carpeta, arch))

            texto = abrir.read()

            buscador(texto, arch)



inicio = time()

ruta = "D:\Python\Dia 9\Mi_Gran_Directorio"
list = []


print(fecha())

print("-" * 30)
print("Archivo \t\tNRO.SERIE")
print("--------- \t\t"*2)

recorrerCarpeta(ruta)

for l in list:
    print(l)
print("-" * 30)
final = time()
time = final -inicio

print(f"Números encontrados: {len(list)}")
print(f"Duración de la búsqueda: {ceil(time)}")