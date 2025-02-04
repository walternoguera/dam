'''cuadrados = []
for i in range(10):
    cuadrados.append(i**2)

print(cuadrados)

cuadrados = [i**2 for i in range(10) if i %2 != 0]
print (cuadrados)

cubos = [i**3 for i in range(10)]
print(f"El cubo es: {cubos}")

#filtramos numeros mayores que 5
cubos = [i**3 for i in range(10) if i > 5]
print(f"Los cubos mayores que 5 son: {cubos}")'''

preguntas = [('nombre', 'objetivo', 'sistema operativo'), 
             ('Juan', 'aprender Python', 'Windows'), 
             ('Ana', 'aprender Python', 'Linux'), 
             ('Pedro', 'análisis de datos', 'MacOS')]

# Usar zip para combinar las preguntas con las respuestas
respuestas = [{pregunta: respuesta for pregunta, respuesta in zip(preguntas[0], respuesta)} for respuesta in preguntas[1:]]
print(respuestas)
