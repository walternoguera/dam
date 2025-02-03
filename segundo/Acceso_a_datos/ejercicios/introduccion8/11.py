'''11. Crea de programa que genere contraseñas.
Para ello, deberás tener 3 tuplas de las que se cogerán los elementos que formarán las
contraseñas.
\ Tupla con dígitos: tupla que contiene los dígitos del 0 al 9
\ Tupla con letras: tupla que contiene las letras del abecedario (sin la letra ñ)
\ Tupla con caracteres especiales: tupla que contiene al menos 15 caracteres
especiales, los que consideresb(¡”$%&/()=…...)
Especificaciones:
\ La contraseñas generadas deberán ser también tuplas.
\ Se generarán dos contraseñas, una fuerte y una débil.
\ El usuario decide por teclado la longitud de la contraseña, mínimo 8
caracteres y máximo 64.
\ La contraseña fuerte deberá tener una compensación aproximada según la
siguiente distribución:
- Un 20% de dígitos, un 40% de letras y un 40% de caracteres especiales.
\ La contraseña débil deberá tener una compensación aproximada según la
siguiente distribución:
- Un 80 % dígitos, un 15% letras y un 5% caracteres especiales.'''

import random as r

def generar_pass(tam):
    passw = ()
    for i in range(tam):
        if i < tam * 0.2:
            passw += (r.choice(digitos),)
        elif i < tam * 0.6:
            passw += (r.choice(letras),)
        else:
            passw += (r.choice(caracteres),)
    return passw

digitos = tuple(range(10))
letras = tuple("abcdefghijklmnopqrstuvwxyz")
caracteres = tuple("!\"#$%&/()=")

tam = int(input("Introduce la longitud de la contraseña (mínimo 8, máximo 64): "))
if tam < 8 or tam > 64:
    print("La longitud de la contraseña no es válida")
else:
    passw_fuerte = generar_pass(tam)
    passw_debil = generar_pass(tam)
    print(f"Contraseña fuerte: {passw_fuerte}")
    print(f"Contraseña débil: {passw_debil}")