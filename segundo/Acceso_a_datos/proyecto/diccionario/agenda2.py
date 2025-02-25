#Funciones CRUD
def agregar_contacto(directorio, nombre, telefono, correo):
    directorio.update(
        {nombre: {"Telefono": telefono, "Correo": correo}}
    )
    print(f"Contacto '{nombre}' agregado correctamente.\n")

def buscar_contacto(directorio, nombre):
    contacto = directorio.get(nombre)
    
    if contacto:
        print(f"{nombre} - Teléfono: {contacto['Telefono']} | Correo: {contacto['Correo']}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def eliminar_contacto(directorio, nombre):
    if nombre in directorio:
        del directorio[nombre]
        print(f"El contacto '{nombre}' eliminado correctamente")
    else:
        print(f"No se encontro el contacto'{nombre}")

def actualizar_contacto(directorio, nombre):
    if nombre in directorio:
        nuevo_telefono = input("Nuevo telefono: ") or directorio[nombre]["Telefono"]
        nuevo_correo = input("Nuevo correo: ") or directorio[nombre]["Correo"]
        directorio[nombre] = {"Telefono": nuevo_telefono, "Correo":nuevo_correo}
        print(f"el contacto '{nombre}' actualizado correctamente")

def mostrar_contactos(directorio):
    print("\nDirectorio de contactos:")
    if directorio:
        for nombre, info in directorio.items():
            print(f"{nombre} - Tel: {info['Telefono']} | Correo: {info['Correo']}")
    else:
        print("No hay contactos guardados")


def inicio():
    while True:
        print("\n--- Bienvenido a la Agenda ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Actualizar contacto")
        print("5. Ver todos los contactos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agregar_contacto(directorio, nombre, telefono, correo)
        elif opcion == "2":
            nombre = input("Ingresa el nombre: ")
            buscar_contacto(directorio, nombre)
        elif opcion == "3":
            nombre = input("Ingresa el nombre que deseas eliminar: ")
            eliminar_contacto(directorio, nombre)
        elif opcion == "4":
            nombre = input("Ingresa el nombre que deseas modificar: ")
            actualizar_contacto(directorio, nombre)
        elif opcion == "5":
            mostrar_contactos(directorio)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intentalo de nuevo.")

#Diccionario global para almacenar contactos
directorio = {}

inicio()
