#Minimos y Maximos
"""
menor = min(58,96,59,94,48)
mayor = max(58,96,59,94,48)
print(menor)
print(mayor)
"""
#Cuando es lista
"""
lista = [58,45,66,95,75]
print(max(lista))
print(min(lista))
print(f"El menor es {min(lista)} y el mayor es max(lista)")
"""
#Cuando es un string
"""
nombres = ["Juan","Pablo","Carlos","Alicia"]
print(min(nombres))
print(max(nombres))
nombre = "Carlos"
print(min(nombre)) #Nos muestra la C porque primero busca las mayusculas y luego las minusculas
print(min(nombre.lower()))
"""
#Cuando es diccionario
dic = {"c1":45,"c2":11}
print(min(dic))#Por defecto buscara por la clave menor
print(min(dic.values()))#De esta manera traera el valor minimo

#Ejemplo de max y min
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())

print(edad_minima)
print(ultimo_nombre)