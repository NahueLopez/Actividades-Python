#Con zip podemos combinar diferentes listas, solamente llegara a la cantidad de la lista que tenga menor.
nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]
ciudades = ["Lima","Madrid","Mexico"]

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

