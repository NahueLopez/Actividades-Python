from pathlib import Path
#Con esto creamos un objeto Path
"""
base = Path.home() #Genera la ruta de donde esta el usuario, absoluta al directorio del usuario actual
#print(base)
#guia = Path("Argentina","Mar del Plata") #Constuye objetos como una ruta
#guia = Path(base, "Argentina","Mar del Plata.txt") #Constuye objetos como una ruta
guia = Path(base,"America Latina", "Argentina",Path("Buenos Aires","Mar del Plata.txt")) #Se crea un objeto de tipo Path perfecto
guia2 = guia.with_name("Miramar.txt") #con esto creamos una ruta igual, pero cambiamos el archivo base
print(guia)
print(guia2)
"""

#Combinamos dos
"""
base = Path.home()
guia = Path(base, "Argentina","Mar del Plata.txt") #Con esto vamos llegando a un nivel mas alto
print(guia.parent)
"""
#Para recorrer entre carpetas los archivos de textos
"""
base = Path.home()
guia  = Path(Path.home(),"Europa")

#for txt in Path(guia).glob("*.txt"): #glob nos muestra todos los archivos que tienen txt en esa carpeta
for txt in Path(guia).glob("**/*.txt"): #Nos trae todos los txt que encuentre en la carpeta principal y todas las demas carpetas que tenga
    print(txt)
"""
#Esto es para traer un camino de carpetas especifico
"""
guia  = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
enEuropa = guia.relative_to(Path("Europa")) #Nos trae la ruta desde ahi para adentro
enEspania = guia.relative_to(Path("Europa","España"))
print(enEspania)
print(enEuropa)
"""
#Como abrir un archivo que es pasado por parametro
"""
from pathlib import Path


def abrir_leer(archivo):
    archivo = open("ejemplo.txt")

    ver = archivo.read()

    archivo.close()

    return ver


archivo = Path('ejemplo.txt')
abrir_leer(archivo)
"""