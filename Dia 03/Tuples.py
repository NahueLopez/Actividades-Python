#Tuple es como la lista pero no se puede editar, al igual que el diccionario puede contener listas,dicc, tuplles y demas
"""
mi_tuple = (1,2,3,4)
t = (1,2.3,"aa")
print(mi_tuple)
print(t)
"""
#Consultar datos
mi_tuple = (1,2,3,4)
print(mi_tuple[0])
print(mi_tuple[-2])

#Para modificar tengo que crear una nueva variable para hacerlo, pero nunca modifico el original
#Consulto datos donde un tuple tiene otro tuple
mi_tuple = (1,2,(10,20),3,4)
print(mi_tuple[2])
print(mi_tuple[2][1])
#Guardo el tuple en una lista
mi_tuple = (1,2,(10,20),3,4)
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
#Asignar contenido de tuple a diferentes variables, Las listas y diccionarios funcionan igual, solo si tiene la misma cantidad de elementos
t = (1,2,3)
x,y,z = t
print(x,y,z)
#El largo del tuplle
t = (1,2,3,4)
print(len(t))
#contamos cuantas veces aparece un valor
t = (1,2,3,2)
print(t.count(2))
#Consultar numero de indice
t = (1,2,3,2)
print(t.index(2))



