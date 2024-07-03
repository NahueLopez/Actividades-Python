#Una forma de controlar si el valor que ingresar es un numero o no
def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break #Para salir del loop

    print("Gracias")

pedir_numero()