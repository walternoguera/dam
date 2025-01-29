'''1.Implementa un programa que muestre los números primos
comprendidos entre 1 y 50.
Ayuda:
Vamos a instalar una librería que nos lo facilita. Seguramente tengas que instalarla:
pip install sympy
Esta librería te facilita si un número es primo o no lo es.'''

from sympy import isprime  # Importamos la función isprime de sympy, esa funcion nos va indicar si un número es primo

def primo(numero):
    return isprime(numero) 

print("Números primos entre 1 y 50:")
for num in range(1, 51):
    if primo(num):  #llamamos a la funcion para verificar si es primo
        print(num)

