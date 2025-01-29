'''3. Realiza un programa que cuente el número de vocales que hay en una cadena de
texto ingresada por el usuario.'''

cadena = input("Ingresa una cadena:")
contador_vocales = 0

for caracter in cadena.lower():
    if caracter in "aeiou":
        contador_vocales += 1
print(f"En el texto {cadena} se encontraron {contador_vocales} vocales.")