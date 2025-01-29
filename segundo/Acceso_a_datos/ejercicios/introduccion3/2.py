'''2. Crea un programa que calcule el factorial de un número ingresado por el usuario
(sin usar recursividad).'''

#pedimos número
numero = int(input("Ingresa un número: "))

factorial = 1 #inicializamos la variable factorial en 1
for i in range(1, numero +1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")