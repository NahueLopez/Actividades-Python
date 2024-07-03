"""Vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta."""

texto = input("Ingrese un texto para analizar: ")
letras = []

letras.append(input("ingrese la primera letra para analizar: ").lower())
letras.append(input("ingrese la segunda letra para analizar: ").lower())
letras.append(input("ingrese la tercera letra para analizar: ").lower())


#1
print("CANTIDAD DE LETRAS")
mtext = texto.lower()
cantidadLetras = mtext.count(letras[0])
cantidadLetras1 = mtext.count(letras[1])
cantidadLetras2 = mtext.count(letras[2])

print(f"Se contro la letra '{letras[0]}' repetida '{cantidadLetras}' veces")
print(f"Se contro la letra '{letras[1]}' repetida '{cantidadLetras1}' veces")
print(f"Se contro la letra '{letras[2]}' repetida '{cantidadLetras2}' veces")



#2
print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Se encontraron un total de '{len(palabras)}' cantidad de palabras")


#3
print("\n")
print("PRIMERA Y ULTIMA LETRA")
primera= texto[0]
ultima = texto[-1]
print(f"La primera letra es '{primera}' y la ultima es '{ultima}'")

#4
print("\n")
palabras.reverse()
textoinvertido = " ".join(palabras)
print(f"Si ordenamos tu texto al revez dira '{textoinvertido}'")

#5
print("\n")
print("Buscando la palabra 'Python' ")
resul = ("Python" in texto)
dic = {True:"Si",False:"No"}
print(f"La palabra 'Python {dic[resul]} se encuentra en el texto")
