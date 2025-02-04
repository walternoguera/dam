nombres = ['Juan', 'Ana', 'Luis', 'María', 'Pedro']
print(nombres[0])
#agregar elementos a la lista

nombres.append('Carlos') #agrega al final
print(nombres)

nombres.insert(1, 'Marta') #agrega en la posición 2
print(nombres)

nombres.remove('Ana') #elimina el primer elemento que coincida con el valor
print(nombres)

nombres.pop(2) #elimina el elemento en la posición 2

del nombres[0] #elimina el elemento en la posición 0
print(nombres)  

nombres.clear() #elimina todos los elementos de la lista
print(nombres)

del nombres #elimina la lista