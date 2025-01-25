'''4. Realiza un programa que calcule la suma de los dígitos de un número entero
ingresado por el usuario.'''

numero = int(input("Ingresa un número entero: "))
suma_digitos = 0

for digito in str(abs(numero)):  #Convertimos el número a cadena para iterar sobre cada dígito
    suma_digitos += int(digito) 

print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
