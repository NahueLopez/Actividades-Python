#Se puede desiganr solo con {} y se divide con (),{},[] o con set (), este no puede tener lista ni dicc
"""
#miSet= set([1,2,3,4,(1,2,3),5,1,1,2,2,3,3,3])
miSet = set((1,2,3,4,5))
#set = {1,3}
#print(type(miSet))
print(miSet)
print(len(miSet))
print(2 in miSet)# Se puede hacer en listas y dic, pero en dic solo las claves
#print(type(set))
#print(set)
"""
#Para unior dos sets, recordar que cuando se repite un numero se ignora el repetido
"""
s1= {1,2,3}
s2= {3,4,5}
s3 = s1.union(s2)
print(s3)
"""
#Metodo add es para agregar un elemento
s1= {1,2,3}
s1.add(4)
print(s1)
#Metodo remove es para eliminar un elemento, si quiere eliminar un elemento que no esta da error
s1= {1,2,3}
s1.add(3)
print(s1)
#Metodo discar es para descargar un elemento , si este no existe no da error
s1= {1,2,3}
s1.discard(4)
print(s1)
#Metodo pop es para eliminar un elemento aleatorio
s1= {1,2,3}
sorte = s1.pop()
print(sorte)
#Metodo clear es para vaciar el set
s1= {1,2,3}
s1.clear()
print(s1)

