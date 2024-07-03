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

piolin = Pajaro("amarillo","Canario")
piolin.piar()
piolin.volar(50)