import re
"""
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"


#palabra = "ayuda" in texto #buscamos si la palabra se encuentra en el texto
#print(palabra)

patron = "ayuda"

busqueda = re.search(patron, texto) #Busca si la palabra esta en el texto
print(busqueda.span()) #Solo la ubicacion de donde esta
print(busqueda.start()) #Solo ubicacion del comienzo
print(busqueda.end())#Solo ubicacion final

#busqueda = re.findall(patron, texto)

for hallazgo in re.finditer(patron, texto): #Nos indica la ubicacion donde esta la palabra
    print(hallazgo.span())
"""
"""
#Buscamos cualquier numero que respete el formato especificado en patron
texto = "llama al 123-525-6588 ya mismo"

#patron = r"\d{3}-\d{3}-\d{4}" #{n} indica la cantidad de veces que se repite
patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

resultado = re.search(patron,texto)
#print(resultado.group()) #Obtenemos el telefono en particular
print(resultado.group(2)) #Nos muestra solamente el conjunto de los numero de grupo que estaban arriba,indice de busqueda por el 1
"""
#Comprobamos que la contraseña tenga lo que necesitamos
"""
clave = input("Clave: ")

patron = r"\D{1}\w{7}" #indicamos que tiene que empezar con un NO numero y luego 7 caracteres mas

chequear = re.search(patron,clave)
print(chequear)
"""

texto = "No atendemos los lunes por la tarde"

#buscar = re.search(r"lunes|martes",texto) #Decimsos que busque si existe lunes o martes en el texto
#buscar = re.search(r"....demos", texto) #Buscamos si cualquier palabra contiene esa palabra,los .. antes y despues indican que cantidad de caracteres va a motrar
#buscar = re.search(r"^\D", texto) #Buscamos que al comienzo no sea un numero
#buscar = re.search(r"\D$",texto)#Nos chequea si hay un digito al final de nuestro string(No numero)
buscar = re.findall(r"[^\s]",texto)#Nos quita todos los espacios vacios
buscar = re.findall(r"[^\s]+",texto)#Cada vez que encuentra un espacio vacio corta la palabra

print(buscar)