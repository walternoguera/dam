'''8- Desempaqueta el valor de cada respuesta almacenada en la tupla del ejercicio
anterior.
Desempaquetar significa sustituir el bucle for del ejercicio anterior que imprimía el
contenido de la tupla, por una función que utilice la siguiente sintaxis:
def desempaquetar_tupla(tupla):
(a, x), (b, y), (c, z) = tupla
print(f"El valor {a} vale {x}")
print(f"El valor {b} vale {y}")
print(f"El valor {c} vale {z}")
de forma que recibe una tupla e imprime por pantalla el contenido de cada par
de elementos que contiene la tupla.'''

mi_tupla = ()
for i in range(3):
    a = input("Introduce una letra para a: ")
    x = input("Introduce un número para x: ")
    mi_tupla += ((a, x),)
print(mi_tupla)

def desempaquetar_tupla(mi_tupla):
    (a, x), (b, y), (c, z) = mi_tupla
    print(f"El valor {a} vale {x}")
    print(f"El valor {b} vale {y}")
    print(f"El valor {c} vale {z}")