'''4. Crea un programa que determine si una palabra es un palíndromo.'''

texto = input("Dime una palabra: ").lower()

if texto == texto[::-1]: #usando slicing, en lugar de poner 1:2:-1, estamos dejando en blanco es decir ::, esto hace que recorra toda la cadena y al incluir -1 estamos diciendo que recorra la cadena hacia atras
    print(f"La palabra ingresada {texto}, es un palíndromo")
else:
    print("No es un palíndromo")

