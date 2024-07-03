#Ponemos todo el texto en mayuscula
texto = "Este es el texto de Nahuel"
resultado = texto.upper()
print(resultado)
#Ponemos en mayuscula solo el indice indicado
texto = "Este es el texto de Nahuel"
resultado = texto[2].upper()
print(resultado)
#Ponemos todo en minuscula
texto = "Este es el texto de Nahuel"
resultado = texto.lower()
print(resultado)
#Separa todo el texto en una lista, cada uno es un elemento separado, tomando por defecto el espacio vacio
texto = "Este es el texto de Nahuel"
resultado = texto.split()
print(resultado)
#Separa todo el texto en una lista, cada uno es un elemento separado, tomando t por separador y no la muestra
texto = "Este es el texto de Nahuel"
resultado = texto.split("t")
print(resultado)
#Unimos las variables
texto = "Aprender"
texto1 = "Python"
texto2 = "es"
texto3 = "genial"
#Lo que ponemos dentro del join con [] es una lista
e = " ".join([texto,texto1,texto2,texto3])
print(e)
#Busca un determinado caracter en un string
texto = "Este es el texto de Nahuel"
resultado = texto.find("s")
print(resultado)
#Sirve para reemplazar un fragmento por otro
texto = "Este es el texto de Nahuel"
resultado = texto.replace("Nahuel","todos")
resultado1 = texto.replace("e","x")
print(resultado,"\n",resultado1)

