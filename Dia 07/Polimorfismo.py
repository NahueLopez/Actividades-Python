#Viene de que los objetos pueden tomar diferentes formas
#Objetos de diferentes clases pueden compartir el mismo metodo y llamarlo desde el mismo lugar pero aplicado a diferentes objetos

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice bee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

#vaca1.hablar()
#oveja1.hablar()

animales = [vaca1,oveja1]
#Creo una lista con los objetos que son diferentes y lo utilizo el metodo en general ya que cada uno de sus objetos tiene su propio metodo
    #for animal in animales:
    #   animal.hablar()

#Creamos una funcion y la utilizamos en ambas instancias creadas siempre que tenga el mismo nombre de metodo
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)