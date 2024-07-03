#En esete caso sacaremos tuples

precios = [("capuchino",1.50),("expreso",2.20),("moka",1.9)]

#for cafe,precio in precios:
 #   print(precio*0.45)
#Que cafe es el mas caro
def cafeMaxCaro(lista):
    precioMayor = 0
    cafeCaro = ""

    for cafe,precio in lista:
        if precio > precioMayor:
            precioMayor = precio
            cafeCaro = cafe
        else:
            pass
    return(cafeCaro,precioMayor)

cafe,precio = cafeMaxCaro(precios)
print(f"El cafe mas caro es :{cafe} cuyo precio es: {precio}")
