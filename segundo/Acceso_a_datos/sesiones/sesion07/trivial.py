import random
import os
import time

rondas = 3
preguntas = [
    ("¿Cuál es la capital de Francia?", "Paris", 5),
    ("¿Cuál es la capital de Alemania?", "Berlin", 5),
    ("¿Cuál es la capital de España?", "Madrid", 5)
]
jugadores = ["Juan", "Ana", "Pedro", "Luis", "María", "José", "Carlos", "Lucía", "Raúl", "Sofía"]

#Diccionario para almacenar el puntaje de cada jugador
puntajes = {jugador: 0 for jugador in jugadores}

#Bucle para las rondas
for i in range(rondas):
    jugador_actual = random.choice(jugadores)

    #Asignamos un puntaje aleatorio inicial al jugador
    puntaje = random.randint(0, 10)

    #Bucle para las preguntas
    for pregunta, respuesta_correcta, puntaje_pregunta in preguntas:
        #Limpiar la pantalla antes de cada pregunta
        os.system('cls' if os.name == 'nt' else 'clear')

        #Imprimir la cabecera con el jugador actual y su puntaje
        print(f"Jugador actual: {jugador_actual} - Puntaje actual: {puntaje}\n")

        #Preguntar al usuario
        respuesta_usuario = input(f"{pregunta}: ")

        #Comparamos la respuesta del usuario con la respuesta correcta
        if respuesta_usuario.strip().lower() == respuesta_correcta.lower():
            print("¡Correcto!")
            puntaje += puntaje_pregunta #Sumamos el puntaje si la respuesta es correcta
        else:
            print("¡Incorrecto!")
            puntaje -= puntaje_pregunta #Restamos el puntaje si la respuesta es incorrecta

        #Pausa para que el usuario vea el resultado antes de limpiar la pantalla
        time.sleep(1)

    #Actualizamos el puntaje del jugador
    puntajes[jugador_actual] = puntaje

    #Imprimimos el puntaje final de ese jugador
    print(f"\nJugador {jugador_actual} - Puntaje final: {puntaje}\n")
    time.sleep(1)

#Determinamos el jugador con el puntaje más altoooo
jugador_ganador = max(puntajes, key=puntajes.get)
print(f"El jugador ganador es {jugador_ganador} con un puntaje de {puntajes[jugador_ganador]}")
