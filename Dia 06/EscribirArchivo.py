#Para escribir linea
"""
archivo = open("prueba1.txt","w")
archivo.write(''' #Para
crear salto de
linea''')
#o
#archivo.write("salto\nlinea")
archivo.close()
"""

#Para escribir por lista
"""
archivo = open("prueba1.txt","w")
archivo.writelines(["Hola","Mundo","estoy","aqui"])
archivo.close()
"""

#Para escribir con un for
"""
archivo = open("prueba1.txt","w")

lista = ["Hola","mundo","estoy","aqui"]

for p in lista:
    archivo.writelines(p + "\n")

archivo.close()
"""

#Para escribir con a
archivo = open("prueba1.txt","a")

archivo.write("Bienvenido")
archivo.close()