miTexto = "Esta es una prueba"
#resultado = miTexto[9]
#resultado = miTexto[-4]

#print(f"En el indice 0 esta la letra {resultado}")
#Tener en cuenta que no es inclusivo el numero, ya que luego de la "a", pondras desde donde comienza y luego hasta donde termina

#resultado = miTexto.index("a",5,11)
#print(f"la letra esta en {resultado}")

#Tambien puede buscar de derecha a izquierda
resultado = miTexto.rindex("a")
print(f"la letra esta en {resultado}")