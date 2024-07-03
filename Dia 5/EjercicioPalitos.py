#Realizaremos un ejercicio donde la persona elijira un numero y luego se le dira si es el palito corto o largo
#Lista Inicial
from random import *

palitos = ["-","--","----","----"]

#Mezclar Palitos
def mezclar(lista):
    shuffle(lista)
    return lista



#Pedirle al usuario que elija un numero
def probarSuerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("Elije un numero del 1 al 4: \n")
    return int(intento)



#Verificar si es el palito mas corto
def chequearIntento(lista,intento):
    if lista[intento -1] == '-':
        print("Te toca lavar los platos")
    else:
        print("Esta vez te haz salvado")

    print(f"Te ha tocado {lista[intento -1]}")

palitosMezclados = mezclar(palitos)
seleccion = probarSuerte()
chequearIntento(palitosMezclados,seleccion)