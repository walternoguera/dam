'''1.Escribe un programa que calcule la suma de los números del 1 al 10.
Ayuda:
En los bucles for, se puede definir un rango, el cual es una secuencia de números.
Puedes generar un rango utilizando la función range().
for numero in range(1, 6): # Esto generará números del 1 al 5
print(numero)'''

suma = 0
for i in range(1,11):
    suma += i

print("La suma de los números de 1  al 10 es:",suma)