"""
diccionario = {"c1":"valor1","c2":"valor1"}
print(diccionario)

resultado = diccionario["c1"]
print(resultado)
"""
#Consulto segun la clave
"""
cliente = {"nombre":"Juan", "apellido":"Fuentes", "peso":88, "talla":176}
consulta = (cliente["talla"])
print(consulta)
"""
#En un diccionario podemos tener listas, otros diccionarios
"""
dic = {"c1":55, "c2":[1,2,3], "c3":{"s1":100,"s2":200}}
print(dic["c2"][1])#Buscamos en la lista el indice 1
print(dic["c3"]["s2"])#Buscamos en el diccionario lo que esta la clave s2
"""
#Mostraremos un resultado en mayuscula
"""
dic = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic["c2"][1].upper())
"""
#Agregaremos contenido al diccionario
"""
dic ={1:"a",2:"b"}
print(dic)

dic[3] = "c"
print(dic)
"""
#Sobreescribimos el contenido al diccionario
dic ={1:"a",2:"b"}
print(dic)
dic[2] = "c"
print(dic)
#Conocer solo las claves
dic ={1:"a",2:"b"}
print(dic.keys())
#Conocer solo los valores
dic ={1:"a",2:"b"}
print(dic.values())
#Conocer todo lo de un diccionario
dic ={1:"a",2:"b"}
print(dic.items())