#Este saca el ultimo elemento del diccionario y lo podes guardar en una variable
"""
dic = {"clave1":100,"clave2":500}

a = dic.popitem()
print(a)
print(dic)
"""
#lstrip elimina de izquierda a derecha los caracteres que digamos
"""
stri = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#")
print(stri)
"""
#Metodo insert() agregar un elemento a una lista, colocando el indice y luego el elemento
"""
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)
"""
#Metodo isdisjoint() esto lo que hace es Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común),
"""
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
"""
#