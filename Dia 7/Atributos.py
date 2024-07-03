#Los atributos pueden cambiar
#Los atributos de clase son los de la clase son iguales para todos
# Luego tenemos los de la instancia

#Creamos un atributo de clase
class Pajaro:

    alas = True #indicamos que los pajaros tienen alas
    #Este metodo construcctor lo va a necesitar ya que son los atributos que va a necesitar
    def __init__(self, color,especie): #self es la convencion indicando de que es cada una de las instancia
        self.color = color #self cada una de las instancias tendra un color
        #El primer color es el atributo el segundo luego del = es el parametro y es el mismo del de arriba
        self.especie = especie

#Creo instancia de pajaro y le asigno el valor que tendra el atributo
mi_pajaro = Pajaro("negro","Canario")

#Imprimo la instancia con el color y especie que le asigne anteriormente
print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print(Pajaro.alas)
print(mi_pajaro.alas)