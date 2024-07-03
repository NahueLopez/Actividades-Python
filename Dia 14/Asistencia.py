import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Creamos una base de datos
ruta = "Empleados"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    image_actual = cv2.imread(f"{ruta}/{nombre}")
    mis_imagenes.append(image_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0]) #Guardamos el nombre sin la extencion

print(nombres_empleados)

# Codificamos las imagenes
def codificar(imagenes):

    #Creamos una lista nueva
    lista_codificada = []

    #Pasamos todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #Codificamos
        codificado = fr.face_encodings(imagen)[0]

        #Agregamos a la lista
        lista_codificada.append(codificado)

    #Devolvemos la lista codificada
    return lista_codificada


#Registrar los ingresos
def registrar_ingresos(persona):
    f = open("registro.csv","r+")#Abrimos el archivo y escribimos
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")#Lo separamos donde encontramos una ,
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f"\n{persona},{string_ahora}")



lista_empleados_codificada = codificar(mis_imagenes)

#Tomamos una imagen de la camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#Leemos la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("No se a podido tomar la captura")
else:
    #Reconocemos la cara en la captura
    cara_captura = fr.face_locations(imagen)

    #Codificamos la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    #Buscamos coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias) #nos da el valor minimo en la lista

        # Mostramos coincidencias si las hay

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            #Buscamos el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1,y1), (x2, y2),
                          (0,255,0),
                          2)
            cv2.rectangle(imagen,(x1,y2 -35), (x2,y2 -35),
                          (0, 255, 0),
                          cv2.FILLED)
            cv2.putText(imagen,nombre, (x1+6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255,255,255))

            #Pasamos la peronsa para guardarlo
            registrar_ingresos(nombre)

            #Mostramos la imagen obtenida
            cv2.imshow("Imagen web", imagen)

            #Mantenemos ventana abierta
            cv2.waitKey(0)