"""tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones."""
#forma 1
"""
nombre = input("Cual es tu nombre: ")
ventas = input("Cuantas son tus ventas: ")
ventas = int(ventas)
comision = round(ventas*13/100,2)

print(f"Tu nombre es {nombre},tus ventas son {ventas} y tu comision es {comision}")
"""
#forma 2
nombre = input("Cual es tu nombre: ")
ventas = int(input("Cuantas son tus ventas: "))
comision = round(ventas*13/100,2)

print(f"Tu nombre es {nombre},tus ventas son {ventas} y tu comision es {comision}")
