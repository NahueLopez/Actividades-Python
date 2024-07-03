#Decoradores - Nos permiten crear diferentes tipos de metodos
#Metodos de instancia
    #def mi_metodo(self):
        #print("algo")
#Metodos de clase -@classmethod - Estos no pueden acceder a los atributos de instancia pero si de clase
    #@classmethod
    #def mi_metodo(cls):
        #print("algo")
#Metodos estaticos @staticmethod - Esto puede ser util para cuando no se puede modificar nada
    #@staticmethod
    #def mi_metodo():
        #print("algo")

#Metodos de instancia
#Se puede acceder y modificar los atributos del objeto
#Pueden acceder a otros metodos
#Puede modificar el estado de la clase
class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        #Estamos agregado un atributo de clase a este atributo
        #a su ves asignamos este metodo al pajaro
        print("pio, mi color es {}".format(self.color))

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")
    #Metodo de clase
    @classmethod#No puedo acceseder a los metodos de atributos anterior
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        #si puedo modificar los de clase como alas
        cls.alas = False
        print(Pajaro.alas)

    #Metodos estaticos
    @staticmethod #Estos metodos no puden modificar los metodos de las instancias ni clase
    def mirar():
        print("El pajaro mira")

#piolin = Pajaro("amarillo","Canario")
#piolin.pintar_negro()
#piolin.volar(50)

#piolin.alas = False
#print(piolin.alas)

#Metodos de Clase - no necesita los self y no puedo acceder a los atributos de instancia
#Pajaro.poner_huevos(3)
#No me deja piar porque necesita un metodo self.
#Pajaro.piar()

#Metodos estaticos
Pajaro.mirar()