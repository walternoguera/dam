'''8. Juego de la patata caliente. Si has visto el Grand Prix este verano sabrás más o menos
de qué se trata, en caso contrario, te lo explico.
Se tiene un tiempo indeterminado, no conocido, aleatorio, en el cual se tendrá que
adivinar un número (entero positivo).
Cuando se inicia el programa, el algoritmo de forma aleatoria marca el tiempo que hay
para adivinar el número, que también es aleatorio.
Especificaciones:
- Tiempo: deberá estar comprendido entre 8 y 15 segundos
- Número: deberá estar comprendido entre 1 y 100 (incluidos)
- Se puede indicar por pantalla, si lo prefieres (no es obligatorio), el tiempo que
hay para adivinar el número.
- Si se termina el tiempo, se indica que se ha terminado el programa y y el
número que se tendría que haber encontrado.
- Si lo encuentras, felicitas al usuario
Os dejo output de ejemplo (no tiene por qué ser exactamente igual):
Tienes 5 segundos para adivinar el número entre 1 y 100.
Adivina el número: 50
El número es menor.
Adivina el número: 25
El número es mayor.
Adivina el número: 35
Se acabó el tiempo. El número era 38.
Ayuda:
Utiliza las librerías time y random.
La librería time (time.time) puede darte el tiempo en segundos desde el 1 de
enero de 1970, UTC.'''


import random
import time

#generamos tiempo y número aleatorio con randint
tiempo_limite = random.randint(8, 15)
numero_secreto = random.randint(1, 100)

print(f"Tienes {tiempo_limite} segundos para adivinar el número entre 1 y 100")

inicio_tiempo = time.time()

while True:
    tiempo_actual = time.time()
    if tiempo_actual - inicio_tiempo > tiempo_limite:
        print(f"Se te acabó el tiempo. El número secreto era {numero_secreto}")
        break #interrumpimos ejecución en caso de que termine el tiempo

    intento = input("Adivina el número: ")
    if not intento.isdigit():
        print("Ingresa un número entero")
        continue
    intento = int(intento)

    if intento == numero_secreto:
        print(f"Haz adivinado el número secreto, el cual es {numero_secreto}")
        break
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")