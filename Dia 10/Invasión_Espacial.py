import pygame
import random
import math
from pygame import mixer
import io
"""
#Evento todo lo que ocurra en la pantallaes un evento
#Forumala para distacia de objeto

"""
#Iniciamos el pygame
pygame.init()

#Creamos en objeto bytes la fuentes
def fuente_bytes(fuente):
    #abre el archivo TTF en modo lectura binaria
    with open(fuente, 'rb') as f:
        #lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        #Crea un objeto bytesIO a partir de los bytes del archivo ttf
    return io.BytesIO(ttf_bytes)



#Creamos la pantalla y el tamaño de la misma. El eje 0,0 se encuentra en la esquina superior izuqierda
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Invasión Espacial")
#Cargamos en la variable el icono que esta en la carpeta, 32 un buen tamaño de icono
icono = pygame.image.load("lanzamiento.png")
#Asignamos el icono con la variable
pygame.display.set_icon(icono)

#Variables del fondo
fondo = pygame.image.load("fondo.jpg")


#Agregar musica
mixer.music.load("musicfondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1) #Suena siempre

balas = []
#Variables del Bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.000000000000000000000000000000000000000000000000001
bala_visible = False


#Variables del Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368 #En donde empieza el jugador en eje x
jugador_y = 500 #En donde empieza el jugador en eje y
jugador_x_cambio = 0

# Variables del Enemigo HACER CLASES LUEGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("enemigo1.png"))
    enemigo_x.append(random.randint(0,736)) #En donde empieza el enemigo en eje x de forma aleatoria
    enemigo_y.append(random.randint(50,200)) #En donde empieza el enemigo en eje y de forma aleatoria
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)


#Variables puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes,35)
texto_x = 10
texto_y = 10

#Texto final ganador
fuente_finalGanador = pygame.font.Font(fuente_como_bytes, 100)
def texto_ganador():
    mi_fuente_finalGanador = fuente_finalGanador.render("Winner", True, (255, 255, 255))
    pantalla.blit(mi_fuente_finalGanador, (200, 200))


#Texto final de juego
fuente_final = pygame.font.Font(fuente_como_bytes, 100)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (180,200))


#Funcion mostrar puntaje
def mostrar_puntaje(x,y):
    #Para mostrar un texto
    texto = fuente.render(f"Puntaje: {puntaje}", True , (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Funcion para que se vea el jugador
def jugador(x, y):
    #Arroja el jugador a la pantalla
    pantalla.blit(img_jugador, (x, y))



#Funcion para que se vea el jugador
def enemigo(x, y, enemig):
    #Arroja el jugador a la pantalla
    pantalla.blit(img_enemigo[enemig], (x, y))


#Funcion para disparar bala
def disparar_bala(x,y):
    global bala_visible #Hacemos global la variable
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))#Mostramos la bala en pantalla


#Funcion detectar colisiones
def hay_colision(x_1, y_1 , x_2, y_2):
    #cuenta de distancia
    #Formula es: distancia = Raiz cuadrada de todo((x2 - x1)^2 +(y2 - y1)^2)
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False





# Loop del juego
se_ejecuta = True
while se_ejecuta:

    #Imagen de fondo
    pantalla.blit(fondo, (0,0))

    #Iterar eventos
    for evento in pygame.event.get():
        #Evento cerrar programa
        if evento.type == pygame.QUIT: #pygame.QUIT es cuando se da click en la [X] de salir
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN: #si se preciono una tecla
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

            if evento.key == pygame.K_SPACE:
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.set_volume(0.3)
                sonido_bala.play()


        #Evento soltar flechas
        if evento.type == pygame.KEYUP: #preguntamos si se solto una tecla
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 0

    #Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    #Mantener dentro de bordes jugador
    if jugador_x <= 5:
        jugador_x = 5
    elif jugador_x >=731:
        jugador_x = 731

    # Modificar ubicacion del enemigo
    if puntaje <= 10:
        for e in range(cantidad_enemigos):

            #Fin del juego muerte del jugador
            if enemigo_y[e] > 500:
                for k in range(cantidad_enemigos):
                    enemigo_y[k] = 1000
                texto_final()
                break

            enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes enemigo
            if enemigo_x[e] <= 5:
                enemigo_x_cambio[e] = 0.3
                enemigo_x_cambio[e] = 0.3
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 731:
                enemigo_x_cambio[e] = -0.3
                enemigo_y[e] += enemigo_y_cambio[e]

            # Colosion
            for bala in balas:
                colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
                if colision_bala_enemigo:
                    sonido_colision = mixer.Sound("explotar.mp3")
                    sonido_colision.play()
                    balas.remove(bala)
                    puntaje += 1

                    enemigo_x[e] = random.randint(0, 736)
                    enemigo_y[e] = random.randint(20, 200)
                    break

            enemigo(enemigo_x[e], enemigo_y[e], e)
    else:

          texto_ganador()



    #Movimiento bola
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)



    #Llamamos a las funciones del jugador y enemigo
    jugador(jugador_x,jugador_y)


    #Mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)

    #Actualizar todo
    pygame.display.update()