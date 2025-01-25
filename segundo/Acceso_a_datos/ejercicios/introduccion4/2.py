'''2. Realiza un programa que calcule la suma de los dígitos de un número entero
ingresado por el usuario. Es decir, el usuario introduce por ejemplo el 123 por teclado, y
la salida deberá ser 1+2+3=6'''

numero = int(input("Ingresa un número entero: "))

#convertimos en valor absoluto con abs, esto va convertir en positivo los números ingresados 
numero = abs(numero)
suma_digitos = 0

while numero > 0:
    digito = numero % 10 
    suma_digitos += digito
    numero //= 10

print(f"La suma de los dígitos es: {suma_digitos}")