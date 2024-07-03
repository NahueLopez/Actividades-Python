import os
import shutil
import send2trash

"""
print(os.getcwd()) #Con esto se donde estoy

archivo  = open("curso.txt","w")
archivo.write("Texto de prueba")
archivo.close()
#Nos muestra los archivos que tenemos en el directorio
print(os.listdir())

#Con esto movemos archivos,
shutil.move("curso.txt", "C:\\Users\\Nahue\\Desktop")

#Con esto borramos el archivo pero lo enviamos a la papelera
send2trash.send2trash("curso.txt")

"""
#os.walk crea duplas con la info
#print(os.walk("D:\\Python"))
#Esto es para recorrer carpetas y archivos
ruta = "D:\Python"

for carpeta, subcarpeta , archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t {sub}")
    print("Los archivos son:")
    for arch in archivo:
        if arch.startswith("b"): #Mostramo solos los archivos que empiecen con b
            print(f"\t {arch}")

