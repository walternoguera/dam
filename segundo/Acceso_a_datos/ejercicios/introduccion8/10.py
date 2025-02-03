'''10. Dada una tupla de tuplas que contiene valores de distintas ciudades y sus
temperaturas en los últimos días, crea un programa que busque si una ciudad específica
está en la tupla y devuelva la media de todas las temperaturas registradas para esa
ciudad.
Ejemplo:
ciudades_temperaturas = (("Madrid", (30, 32, 31)), ("Barcelona", (20, 26, 21)), ("Valencia", (28, 29, 27)))
Barcelona -> 22,3'''

ciudades_temperaturas = (("Madrid", (30, 32, 31)), ("Barcelona", (20, 26, 21)), ("Valencia", (28, 29, 27)))
ciudad = input("Introduce una ciudad: ")
for i in ciudades_temperaturas:
    if ciudad in i:
        media = sum(i[1]) / len(i[1])
        print(f"{ciudad} -> {media}")
        break
else:
    print("La ciudad no está en la tupla")