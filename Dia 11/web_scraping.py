import bs4 #Nos permite navegar por todo el texto y nos permite buscar lo que necesitamos
import requests
"""
Realizamos la busqueda en una web
"""
resultado = requests.get("https://www.escueladirecta.com//")

#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

#print(sopa.select('title')[0].getText()) #Permite traer lo que esta en title, en la posicion 0 para no traer nada mas
# ese valor de string y a su vez con el .getText() solamente traemos el texto

#parrafo_espacial = sopa.select('p')[3].getText()
#print(parrafo_espacial)

#columna_lateral = sopa.select(".container p") #Obtengo todo lo que tiene la clase container, todos los parrafos de la columna
#print(columna_lateral)

imagenes = sopa.select(".course-box-image")[0]["src"] # trae todo lo que tenga una imagen

print(imagenes)
imagen_curso_1 = requests.get(imagenes)
#print(imagen_curso_1.content)

f = open("mi_imagen.jpg", "wb")
f.write(imagen_curso_1.content)
f.close()