#Antes

serie = "N-02"
"""
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese numero de serie")
"""
#Con el Match
"""
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese numero de serie")
"""

cliente = {"nombre":"Nahuel",
           "edad":28,
           "ocupacion":"capacitador"
           }
pelicula = {"titulo":"Matrix",
            "fichaTecnica": {"protagonista":"Keanu reeves",
                             "directora":"Lana y Lilly Wachowski"
                            }
            }
elementos = [cliente,pelicula,"libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo": titulo,
              "fichaTecnica":{"protagonista":protagonista,
                              "directora":director}}:
            print("Esto es una Pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")