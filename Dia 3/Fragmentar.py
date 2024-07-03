texto = "ABCDEFGHIJKLM"
#Fragmenta desde el indice 2 hasta que termine
fragmento = texto[2]
print(fragmento)
#Fragmenta desde el indice 2 hasta el 5 no inclusive
fragmento = texto[2:5]
print(fragmento)
#Fragmenta desde el indice 0 hasta el 5
fragmento = texto[:5]
print(fragmento)
#Fragmenta desde el indice 2 hasta el 10, pero salteando de 2 en 2
fragmento = texto[2:10:2]
print(fragmento)
#Tenemos la cadena de manera al revez
fragmento = texto[::-1]
print(fragmento)
#Tenemos la cadena de manera al revez pero salteando de 2
fragmento = texto[::-2]
print(fragmento)
