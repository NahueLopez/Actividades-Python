from os import system #Esto es para importar lo que necesitamos para limpiar la consola
#Ademas tenemos que ir a run - debug - editar configuracion - execution - tildad emulator
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system("cls")

print(f"Tu nombre es {nombre} y tienes {edad} años")