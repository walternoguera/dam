'''8. Crea un programa que simule un juego de adivinanza, donde el usuario debe
adivinar un número aleatorio generado por la computadora.'''

import random

numero_aleatorio = random.randint(1, 100)

print("=====Bienvenido al juego de adivinanza=====")
print("Estoy pensando en un número entre 1 y 100, adivina cual es")

intentos = 0

adivina = int(input("Ingresa el número: "))

# Repetir mientras no adivine
while adivina != numero_aleatorio:
    intentos += 1
    if adivina < numero_aleatorio:
        print("Demasiado bajo. prueba de nuevo")
    elif adivina > numero_aleatorio:
        print("Demasiado alto. prueba de nuevo")
    adivina = int(input("Ingresa el número: "))

# Cuando adivine
intentos += 1
print(f"Adivinaste el número en {intentos} intentos.")
