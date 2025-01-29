'''9. Para terminar, volvemos al ejercicio número 1, pero esta vez sin librería que nos lo
facilite.
Ayuda:
Implementa una función, “Es_Primo(Numero)”, que reciba un número entero.
Deberás tener en cuenta que los números menores de 2 NO son primos.
Hay que calcular desde el primer número primo hasta el número correspondiente
a la raíz cuadrada de “Numero”.
La razón, te la tendrás que creer ya que te la da tu compañero matemático, de
usar la raíz cuadrada es que si “Numero” tiene un divisor (es divisible con resto
cero) mayor que su raíz cuadrada, también tendrá un divisor menor que su raíz
cuadrada, por lo que no es necesario comprobar más allá de la raíz cuadrada.
Por si te sirve, una definición más técnica es que se debe a que los divisores
vienen en pares. Por ejemplo, si d es un divisor de n, entonces n / d también es
un divisor de n.
Si ambos divisores fueran mayores que la raíz cuadrada de n, su producto sería
mayor que n, lo cual es imposible.
Esto reduce significativamente el número de comprobaciones necesarias,
haciendo el algoritmo más eficiente.
Para calcular la raíz cuadrada, puedes hacer: Numero**0.5
Te pongo un ejemplo más fácil:
Supongamos que Numero es 36.
Sus divisores son 1, 2, 3, 4, 6, 9, 12, 18 y 36 (igual que en el ejercicio de MCD).
Ten en cuenta que la raíz cuadrada de 36 es 6 (6*6=36)
Observa que los divisores menores o iguales a la raíz cuadrada de 36 (que es 6)
son 1, 2, 3, 4 y 6. (fíjate que el 6 está incluido)
Los divisores mayores que 6 (9, 12, 18 y 36) son simplemente los resultados de
dividir 36 por los divisores menores o iguales a 6 (sus pares)
Por lo tanto, si no encuentras ningún divisor de Numero hasta su raíz cuadrada,
puedes estar seguro de que Numero no tiene otros divisores y, por lo tanto, es
primo.'''


#definimos la funcion Es_primo
def Es_primo(numero):
    if numero < 2:
        return False
    
    for dividor in range(2, int(numero**0.5) + 1):
        if numero % dividor == 0:
            return False
    return True #si no encuentra divisores entonces el numero es primo

numero = int(input("Ingresa un número para verificar si es primo: "))
if Es_primo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")