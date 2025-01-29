'''6. Realiza un programa que simule el juego de "Piedra, Papel o Tijeras" contra el
ordenador.'''

import random

print("=== Juego: Piedra, Papel o Tijeras ===")

for i in range(5):
    print(f"\nRonda {i + 1}:")
    
    usuario = input("Elige una de las opciones: piedra, papel, tijeras: ").lower()

    if usuario not in ["piedra", "papel", "tijeras"]:
        print("Elige una de las opciones válidas")
        continue 

    opciones = ["piedra", "papel", "tijeras"]
    pc = random.choice(opciones)
    print(f"El ordenador eligió: {pc}")

    if usuario == pc:
        print("¡Empate!")
    elif (usuario == "piedra" and pc == "tijeras") or (usuario == "papel" and pc == "piedra") or (usuario == "tijeras" and pc == "papel"):
        print("Ganaste")
    else:
        print("Perdiste")
