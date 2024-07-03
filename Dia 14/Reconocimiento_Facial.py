import cv2
import face_recognition as fr

# Cargamos las imagenes
foto_control = fr.load_image_file("FotoA.jpg")
foto_prueba = fr.load_image_file("FotoG.jpg")


#Pasamos las imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control A
lugar_cara_A = fr.face_locations(foto_control)[0] #Indicamos que es el primer elemento siempre(en este caso)
cara_codificada_A = fr.face_encodings(foto_control)[0]#Codificamos la imagen

# Localizar cara control B
lugar_cara_B = fr.face_locations(foto_prueba)[0] #Indicamos que es el primer elemento siempre(en este caso)
cara_codificada_B = fr.face_encodings(foto_prueba)[0]#Codificamos la imagen


#print(lugar_cara_A) #Vemos los pixeles de la cara

#mostramos rectangulo A
cv2.rectangle(foto_control,
              (lugar_cara_A[3],lugar_cara_A[0]),
              (lugar_cara_A[1],lugar_cara_A[2]),
              (0, 255, 0),
              2)


#mostramos rectangulo B
cv2.rectangle(foto_prueba,
              (lugar_cara_A[3],lugar_cara_B[0]),
              (lugar_cara_A[1],lugar_cara_B[2]),
              (0, 255, 0),
              2)

#Localizamos comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

#print(resultado) # Veiamos en consola el resultado

# Medida de la distancia para verificar si es el mismo o no
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
#print(distancia) #Veiamos la distancia que existe

#Mostramos resultado
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)



# Mostramos las imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

#Mantenemos programa abierto hasta que se precione una tecla
cv2.waitKey(0)