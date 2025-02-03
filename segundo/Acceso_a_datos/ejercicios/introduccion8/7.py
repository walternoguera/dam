'''7- Implementa, usando un bucle for, la tupla ahora tenga el par de valores (a,b),
de forma que:
mi_tupla=((a,x),(b,y),(c,z))
donde a,b,c son letras introducidas por teclado y x,y,z son números.
El resultado al imprimir la tupla deber ser del tipo:
el valor a vale x,
el valor b vale y,
el valor c vale z
¡¡Sustituyendo cada uno de ellos por el valor introducido por teclado!!'''

mi_tupla = ()
for i in range(3):
    a = input("Introduce una letra para a: ")
    x = input("Introduce un número para x: ")
    mi_tupla += ((a, x),)
for i in mi_tupla:
    print(f"El valor de {i[0]} es {i[1]}")