"""
Vamos a comprimir y descomprimir
"""
import zipfile
"""
#De esta forma comprimimos los archivos y los guardamos en "archivo_comprimido"

mi_zip = zipfile.ZipFile("archivo_comprimido.zip","w") #Creamos un archivo zip

mi_zip.write("Texto_A.txt")
mi_zip.write("Texto_B.txt")

mi_zip.close()

#De esta manera descompimimos los archivos que esten en la carpeta
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip","r")

zip_abierto.extractall()
"""

import shutil
"""
#Comprimimos archivos y carpetas completas

carpeta_origen = "D:\Python"

archivo_destino = "Todo_Comprimido"

shutil.make_archive(archivo_destino, "zip", carpeta_origen)

#Descomprimimos el archivo
shutil.unpack_archive("Todo_Comprimido.zip","Extraccio Terminada", "zip")
"""
zip_abierto = zipfile.ZipFile("Proyecto+Dia+9.zip","r")

zip_abierto.extractall()

abrir = open("Instrucciones.txt","r")

print(abrir.read())
abrir.close()