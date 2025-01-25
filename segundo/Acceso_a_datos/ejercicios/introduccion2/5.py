'''5. Escribe un programa que sume los números pares del 1 al 100'''

pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        pares += numero

print("La suma de los números pares del 1 al 100 es: ", pares)