#Este nos permite poder recibir un cantidad ilimitada de argumentos, pero tiene nombre y elemento, podemos acceder a el mediante un diccionario y podemos ver el indice
"""
def suma(**kwargs):

    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return(total)

print(suma(x=3, y=5, z=2))#lo envio asi nomas, y cuando lo recibe lo transforma en dic
"""
"""
def prueba(num1,num2,*args,**kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg es = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400]
kwargs = {"x":"uno","z":"dos","z":"tres"}

prueba(15,50,*args,**kwargs)
#prueba(15,50,100,200,300,400,x="uno",y="dos",z="tres")
"""
#Ejercicio
"""
def lista_atributos (**kwargs):
    l = []
    for clave,valor in kwargs.items():
        l.append(valor)
    return(l)

print(lista_atributos(x="uno",y="dos",z="tres"))
"""
#Ejercicio

def describir_persona(nombre, **kwargs):

    print(f"Características de {nombre}:")

    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")