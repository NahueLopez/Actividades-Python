#*args = argumentos variables que el usuario decida pasar
"""
def suma(*args):#la palabra args se puede cambiar, ya que lo que importa es el * pero se recomienda usar args
    #forma antigua
    total = 0
    for n in args:
        total += n

    return sum(args) #Version corta del codigo anterior

print(suma(5,5,6)) #No importa cuantos parametros pasemos, que los va a recorrer y sumar
"""
#Que tome todos los valores y los sume, sin importar el signo, a todos los transforma en positivo
"""
def suma_absolutos(*args):
    total = 0
    for n in args:
        if n < 0:
            n = n * -1
            total += n
        else:
            total += n
    return(total)

print(suma_absolutos(1,-2))
"""
#Recivir un nombre y un *args, devolver un mensaje

def numeros_persona (nombre,*args):
    suma_numeros = sum(args)
    print(nombre,suma_numeros)

