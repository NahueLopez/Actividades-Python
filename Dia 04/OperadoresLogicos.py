#Comprar mas de un resultado con and ( y )
"""
miBol = (4 < 5) and (5 > 6) #Se tienen que cumplir ambas condiciones para que de true
miBol = (55 == 55) and ("perro" == "perro") #Se pueden comparar varios typos al mismo tiempo
print(miBol)
"""
#Comprar mas de un resultado con or ( o )
"""
miBol = 10 == 10 or 3 == 3 #Con que se de una de las 2 sea verdad nos dara True,
miBol = 10 == 9 or 3 == 0 #Solamente si las 2 son falsas dara False
print(miBol)
"""
#Tambien funciona para buscar una palabra en un texto
"""
texto = "esta frase es breve"
miBol = ("frase" in texto) and ("breve" in texto) #La palabra tiene que estar en ambos para que de True
print(miBol)
miBol = ("frase" in texto) or ("python" in texto) #La palabra con solo estar en 1 dara True
print(miBol)
"""
#Comparar con un not, este no dira si NO es verdad la comparacion, Niega la comparacion normal
"""
miBol = "a" == "a"
print(miBol)
miBol = not ("a" == "a")
print(miBol)
miBol = not ("a" != "a")
print(miBol)
"""