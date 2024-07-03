import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Diferentes voces / idiomas
id1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id4="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"


#Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #Almacenamos el recognizer en una variable
    r = sr.Recognizer()

    # Configuramos el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera para que empiece a escuchar
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puede hablar")

        #Guardamos en variablo lo que escucha como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # Prueba de que pudo ingresar la voz
            print("Dijiste: " + pedido)

            # Devolvemos a pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #Prueba de que no comprendio el audio
            print("Ups, no entendi")

            #Devolvemos el error
            return "Sigo esperando"

        #en caso de que no puedo convertirlo en string
        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # Devolvemos el error
            return "Sigo esperando"

        #Error inesperado
        except:

            # Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # Devolvemos el error
            return "Sigo esperando"


#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id4)

    #Pronuncie el mensaje
    engine.say(mensaje)
    engine.runAndWait()


#Informar el dia de la semana
def pedir_dia():

    #Creamos la variable del dia de hoy
    dia = datetime.date.today()
    numero_dia = dia.day
    print(dia)

    #Creamos una variable para el dia de la semana
    dia_semana = dia.weekday() #Nos dice que dia es , lunes...
    print(dia_semana)

    #diccionario con nombres de dias
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    #decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]},{numero_dia}")


#Informamos que hora es
def pedir_hora():

    #Creamos una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las: {hora.hour} horas,con {hora.minute} minutos"
    print(hora)

    #Decir la hora
    hablar(hora)

# Funcion de Saludo Inicial
def saludo_inicial():

    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"

    #Decir el saludo
    hablar(f"{momento} Nahue, soy Helena, tu asistente personal. Por favor, decime en que puedo ayudarte")

# Funcion central del asistente
def pedir_cosas():

    #Activamso el saludo inicial
    saludo_inicial()

    #Creamos variable de corte
    comenzar = True

    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if "abri youtube" in pedido:
            hablar("Con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abri google" in pedido:
            hablar("Con gusto, estoy abriendo el navegador")
            webbrowser.open("https://www.google.com/")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple" : "APPL",
                       "amazon" : "AMZN",
                       "google" : "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif "chao" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()