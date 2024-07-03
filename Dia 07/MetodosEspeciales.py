#Estos metodos son especiales y no se pueden acceder con los metodos normales

#mi_lista = [1,1,1,1,1,1,]

#print(len(mi_lista))
#print(mi_lista)
#class Objeto:
 #   pass

#mi_objeto = Objeto()
#No se puede con leer ver la cantidad de objetos que tengo en la lista
#print(len(mi_objeto))
#print(mi_objeto)

class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    #De esta forma podemos hacer que cuando llamo a la instancia se ve a de esta manera
    def __str__(self):
        return f"Album:{self.titulo} de {self.autor}"

    #De esta manera puedo definir como sera el largo de mi objeto
    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD("Pink Floyd","The Wall",24)

print(mi_cd)
print(len(mi_cd))

#De esta menera eliminamos los objetos
del mi_cd

