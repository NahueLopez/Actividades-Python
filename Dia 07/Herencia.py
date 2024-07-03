#Se pueden heredar algunos atributos creando una clase hija de una padre esta puede sobreescribir nuevos atributos
#Es para mejorar el codigo y no repetirlo tanto

#Creamos la herencia
class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
     pass

#print(Pajaro.__bases__) #De esta forma sabemos que la clase Pajaro hereda de donde
#print(Animal.__subclasses__()) #De esta forma sabemos que clases tienen herencia de esta class

piolin = Pajaro(2,"amarillo")
#piolin.nacer() #De esta manera podemos ver que el metodo lo podemos usar y que es del padre
print(piolin.color)