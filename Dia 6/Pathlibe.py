from pathlib import Path, PureWindowsPath


carpeta = Path("C:/Users/Nahue/Desktop/Estudios/Analista/MATEMATICA.txt") #Nos permite abrir un archivo sin necesidad de open y close
#print(carpeta.read_text()) #Para mostrar el contenido
#print(carpeta.name) #Nos trae el nombre del archivo
#print(carpeta.suffix) #Nos trae que tipo de archivo es (txt)
#print(carpeta.stem) #Nos trae el nobmre sin la extencion (txt)

#Nos muestra la ruta para window
#rutaWindos = PureWindowsPath(carpeta)
#print(rutaWindos)

#Para verificar si existe o no

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Si existe")