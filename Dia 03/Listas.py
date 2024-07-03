#Todo lo aplicado en indces sirve para listas
"""
miLista = ["a","b","c"]
miLista2 = ["d","e","f"]
resultado = len(miLista)
print(resultado)
resultado = miLista[0]
print(resultado)
print(miLista + miLista2)
#o
miLista3 = miLista + miLista2
print(miLista3)
"""
#Alterar los elementos, sobreescribimos el indice 0, pero se puede con cualquiera
"""
miLista = ["a","b","c"]
miLista2 = ["d","e","f"]
miLista3 = miLista + miLista2
miLista3[0] ="alfa"
print(miLista3)
"""
#Con append le agregamos un nuevo elemento a la lista,es para agregar elementos
"""
miLista = ["a","b","c"]
miLista2 = ["d","e","f"]
miLista3 = miLista + miLista2
miLista3.append("g")
print(miLista3)
"""
#Con pop le eliminamos un  elemento a la lista,si no le ponemos nada dentro del () borrara el ultimo elemento
"""
miLista = ["a","b","c"]
miLista2 = ["d","e","f"]
miLista3 = miLista + miLista2
eliminando = miLista3.pop(0) #Con esto vamos a mostrar el elemento eliminado
print(eliminando)
"""
#Esto es para ordenar por orden alfavetico, funciona con numero tambien, NO se puede guardar, ya que solo sirve para mostrar
"""
lista = ["g","o","b","m","c"]
lista.sort()
print(lista)
"""
#Esto es para dar vuelta el orden , de ultimo a primero, es igual al anterior no se puede almacenar
lista = ["g","o","b","m","c"]
lista.sort()
lista.reverse()
print(lista)