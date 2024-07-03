class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta,balance =0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Tu nombre es {self.nombre} y apellido {self.apellido}, su numero de cuenta es {self.numero_cuenta} y su balance es {self.balance}"

    def depositar(self,monto):
        self.balance += monto
        print("Deposito aceptado")
        print(f"El balance actual es de {self.balance}")

    def retirar(self,monto):
        if monto <= self.balance:
            self.balance -= monto
            print("Deposito Aceptado")
            print(f"Su balance actual es de {self.balance}")
        else:
            print("El monto a retirar es mayor a su balance")
            print(f"Su balance actual es de {self.balance}")
def crear_cliente():


    nombre = input("Coloque su nombre: ")

    apellido = input("Coloque su apellido: ")

    numero_cuenta = input("Coloque su numero de cuenta: ")

    cliente= Cliente(nombre,apellido,numero_cuenta)

    return cliente

def deposito(mi_cliente):

    cantidad = "x"

    while not cantidad.isnumeric():
        print("Coloque el monto a depositar")
        cantidad = input()

        mi_cliente.depositar(int(cantidad))

def retirar(mi_cliente):
    cantidad = "x"

    while not cantidad.isnumeric():
        print("Coloque el monto a retirar")
        cantidad = input()

        mi_cliente.retirar(int(cantidad))
def inicio():

    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != "S":
        print("Elije una opcion: Depositar [D] - Retirar [R] o Salir [S]")
        opcion = input()

        if opcion == "D":
            deposito(mi_cliente)
        elif opcion == "R":
            retirar(mi_cliente)
        elif opcion == "S":
             #dalir
            pass

inicio()