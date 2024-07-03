#Para controlar los errores y que no se detenga el programa por completo
#Se hace mediante intentar, excepcion y finalmente
#Se utiliza es try: intenta esto
#except : si se genera un error utiliza esto
#finaly: no importa si hay un error, pero ejecuta esto

def suma():

    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))

    print(n1 + n2)
    print("Gracias por sumar" + n1)


"""
try:
    #codigo que queremos probar
    
except:
    #codigo a ejecutar si hay un error
    
else: #No siempre se usa 
    #Se puede agregar este, si es el codigo que se ejecute si no hay un error
    
finally: #No siempre se usa
    #codigo que se ejecuta de todos modos
    
"""
"""
try:
    suma()
except:
    print("Algo no salio bien")
else:
    print("Hiciste todo bien")
finally:
    print("Muchas gracias")
"""
"""
try:
    suma()
except TypeError: #De esta menera indicamos que mostrar en este tipo de error.
    print("Estas intentando concatenar tipos distintos")
except ValueError: #De esta menera indicamos que mostrar en este tipo de error.
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Muchas gracias")
    """