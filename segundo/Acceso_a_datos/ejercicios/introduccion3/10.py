'''10. Realiza un programa que cuente cuántas vocales hay en una cadena de texto
ingresada por el usuario.'''

texto = input("Ingresa una cadena de texto: ")
contador_vocales = 0

for caracter in texto.lower():  #convertimos con lower a minúsculas para evitar errores
    if caracter in "aeiou":  # verificamos si el caracter es una vocal
        contador_vocales += 1

print(f"La cantidad de vocales en el texto ingresado es: {contador_vocales}")
