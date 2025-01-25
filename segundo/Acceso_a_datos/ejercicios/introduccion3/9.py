'''9. Diseña un programa que calcule el promedio de una lista de números ingresados
por el usuario.'''

numeros = input("Ingresa los números separados por espacio: ")

numeros = numeros.split()  #con split convertimos los numeros ingresados en una lista
total = 0 
cantidad = 0

#sumamos los números y contamos cuantos hay
for numero in numeros:
    total += int(numero)  #convertimos cada número a entero y lo sumamos
    cantidad += 1 

#10Calculamos el promedio
promedio = total / cantidad

print(f"El promedio es: {promedio}")
