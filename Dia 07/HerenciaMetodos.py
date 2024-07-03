#La herencia se puede modificar o algunos no obtenerlos
#Herencia multiple tambien y la herencia se puede ampliar y multiplicar
#Si se hereda un metodo y creamos otro igual va a utilizar en de la clase y no el de la herencia
#Se pueden agregar nuevos atributos propios de la clase hererada

class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
    #    self.edad = edad
     #   self.color = color

    #Con el super traemos los metodos padres para modificarlos sin necesidad de repetir
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")



piolin = Pajaro(3,"amarillo",60)
mi_animal = Animal(2,"atrigado")
#piolin.hablar()

piolin.volar(199)
