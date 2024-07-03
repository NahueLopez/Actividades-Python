#def indica que estamos creando una funcion
#Se recomienda luego de la funcion anotar que es el texto
"""
def saludar_persona(nombre):
    #Esta funcion es para saludar
    print("Hola " + nombre )

saludar_persona("Nahuel")
"""
#Retornando un valor
"""
def multiplicar(num1,num2):
    #return num1 * num2
    total= num1 * num2
    return total
#print(multiplicar(5,10))
resultado = multiplicar(5,10)
print(resultado)
"""
#Al recibir una variable a la funcion, pasarla toda a mayuscula y leerla al revez
"""
def invertir_palabra(palabra):
    palabra = palabra.upper()
    textoinvertido = palabra[::-1]
    return textoinvertido


palabra = "Python"

resultado = invertir_palabra(palabra)
print(resultado)}
"""
#Nos chequea si un numero es de 3 cifras
"""
def chequear_3_cifras(numero):
    return numero in range(100,1000)
suma = 586 + 402
resultado=chequear_3_cifras(suma)
print(resultado)
"""
#Indicarnos si hay algun valor de 3 cifras
"""
def chequear_3_cifras(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

resultado=chequear_3_cifras([555,45,54])
print(resultado)
"""
#Pasa por los 3 siclos
"""
def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([55, 45, 54])
print(resultado)
"""
#Que nos devuelva los numero que coincidan con la condiccion de 3 cifras
"""
def chequear_3_cifras(lista):
    lista3 = []

    for n in lista:
        if n in range(100, 1000):
            lista3.append(n)
        else:
            pass
    return lista3

resultado = chequear_3_cifras([553, 45, 54])
print(resultado)
"""
#En este caso realizamos la suma si el numero esta dentro del parametro
"""
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n > 0 and n < 1000:
            suma = suma + n
        else:
            continue
    return suma


lista_numeros = [1,1000,2,]
suma= suma_menores(lista_numeros)
print(suma)
"""