'''5. Escribe un programa que encuentre el máximo común divisor (MCD) de
dos números ingresados por el usuario.
Ayuda:
El MCD es el número más grande que divide a dos números de manera exacta (sin dejar
residuo o resto)
Sean los números 12 y 8, por ejemplo.
Los divisores de 12 son: 1, 2, 3, 4, 6, 12, ya que al dividir 12 por cualquiera de
esos números el resto = 0.
Los divisores de 8 son: 1, 2, 4, 8 por la misma razón pero respecto al 8.
Si te fijas, los divisores comunes, los que coinciden, entre 12 y 8 son: 1, 2, 4.
De esos tres comunes, el más grande, el máximo común divisor es 4, por lo que el
MCD(12,8)=4'''


num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número:"))

while num2 != 0:
    residuo = num1 % num2
    num1 = num2
    num2 = residuo

print(f"El MCD de los números {num1} y {num2} es: {num1}")