#De esta manera podemos crear herencia, siempre de abajo para arriba
#Vemos ejemplo como se puede heredar de varios padres
#En caso de tener mas de una herencia si se repiten los metodos siempre va a usar la primera que este agregada, va por orden
class Padre:
    def hablar(self):
        print("Hola soy tu padre")

class Madre:

    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Hola soy tu madre")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()
#Forma de ver el orden que viene de herencia
print(Nieto.__mro__)