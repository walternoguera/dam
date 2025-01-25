'''3.Diseña un programa que muestre los números primos entre 1 y 50.'''


print("Números primos entre 1 y 50:")
for numero in range(2, 51):
    primo = True
    for divisor in range(2, numero):  # Comprueba todos los números menores que `numero`
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        print(numero)