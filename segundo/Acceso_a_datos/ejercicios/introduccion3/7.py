'''7. Realiza un programa que muestre los números del 1 al 100, pero que reemplace los
múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz".'''

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:  #Múltiplo de 3
        print("Fizz")
    elif numero % 5 == 0:  #Múltiplo de 5
        print("Buzz")
    else:
        print(numero)
