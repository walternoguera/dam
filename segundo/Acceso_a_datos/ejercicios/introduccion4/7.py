'''7. Implementa las siguientes puertas lógicas:
AND, OR, NOT'''

#ejercicio de calificaciones usando AND
contador = 0
while contador < 5:
    nota1 = float(input("Ingresa la nota del primer examen: "))
    nota2 = float(input("Ingresa la nota del segundo examen: "))

    if nota1 >= 5 and nota2 >= 5:
        print("Aprobaste ambos exámenes")
    elif nota1 >= 5 or nota2 >= 5:
        print("Aprobaste uno de los dos exámenes")
    else:
        if not (nota1 >= 5 or nota2 >= 5):
            print("Reprobaste ambos exámenes")

    contador += 1 
