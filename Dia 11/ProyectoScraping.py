import  bs4
import requests

# Crea una url sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html" #COpio la url y veo que es lo que cambia

#Lista de titulos de 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1, 51):

    # Creamos una sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text , 'lxml')

    #Creamos ua variable de seleccion de la sopa
    libros = sopa.select(".product_pod")

    # Iteramos en los libros
    for libro in libros:

        # Verificamos que tengan 4 o 5 estrallas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # Guardamos el titulo en la variable
            titulo_libro = libro.select("a")[1]["title"]

            # Agregamos los libros a la lista
            titulos_rating_alto.append(titulo_libro)

# Vemos los libros en consola

for t in titulos_rating_alto:
    print(t)