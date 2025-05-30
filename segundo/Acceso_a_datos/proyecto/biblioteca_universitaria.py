import random

# función para normalizar nombres de campus
def normalizar_campus(entrada):
    equivalencias = {
        "ciencia": "Ciencia",
        "tecnologia": "Tecnología",
        "tecnología": "Tecnología",
        "sanitario": "Sanitario",
        "legal": "Legal"
    }
    return equivalencias.get(entrada.strip().lower(), None)

# estructura de la universidad
universidad = {
    "Ciencia": {
        "carreras": ["Biología", "Química", "Física", "Matemáticas", "Geología"],
        "biblioteca": []
    },
    "Tecnología": {
        "carreras": ["Informática", "Ingeniería", "Robótica", "Telecomunicaciones", "Sistemas"],
        "biblioteca": []
    },
    "Sanitario": {
        "carreras": ["Enfermería", "Medicina", "Fisioterapia", "Farmacia", "Odontología"],
        "biblioteca": []
    },
    "Legal": {
        "carreras": ["Derecho", "Criminología", "Relaciones Laborales", "Administración Pública", "Política"],
        "biblioteca": []
    },
    "Rectorado": {
        "carreras": [],
        "biblioteca": []
    }
}

def crear_libro(titulo, autor, año):
    return {"titulo": titulo, "autor": autor, "año": año, "disponible": True}

# libros por campus (resumen)
libros_ciencia = [crear_libro("Física Cuántica", "Luis Torres", "2015")]
libros_tecnologia = [crear_libro("Programación en Python", "Laura Díaz", "2018")]
libros_sanitario = [crear_libro("Enfermería Clínica", "Lucía Romero", "2013")]
libros_legal = [crear_libro("Derecho Penal", "Gabriela Ruiz", "2010")]
libros_rectorado = [crear_libro("Historia del Arte", "Manuel Pérez", "2005") for _ in range(15)]

# asignar libros mezclados para cumplir requisitos
universidad["Ciencia"]["biblioteca"] = libros_ciencia + libros_legal + libros_sanitario
universidad["Tecnología"]["biblioteca"] = libros_tecnologia + libros_ciencia + libros_legal
universidad["Sanitario"]["biblioteca"] = libros_sanitario + libros_tecnologia + libros_legal
universidad["Legal"]["biblioteca"] = libros_legal + libros_ciencia + libros_sanitario
universidad["Rectorado"]["biblioteca"] = libros_rectorado

usuarios = []
reservas = {}

def registrar_usuario():
    nombre = input("Nombre del estudiante: ")
    entrada = input("Campus (Ciencia/Tecnología/Sanitario/Legal): ")
    campus = normalizar_campus(entrada)
    if campus is None:
        print("Campus no válido.")
        return
    carrera = input("Carrera: ")
    contraseña = input("Contraseña: ")

    cantidad = sum(1 for u in usuarios if u["campus"] == campus and u["carrera"] == carrera)
    if cantidad >= 5:
        print("Esta carrera ya tiene 5 estudiantes registrados.")
        return

    id_usuario = f"{nombre}_{random.randint(100, 999)}"
    usuarios.append({"id": id_usuario, "nombre": nombre, "campus": campus, "carrera": carrera, "contraseña": contraseña})
    print(f"Usuario registrado con ID: {id_usuario}")

def baja_usuario():
    id_usuario = input("Introduce tu ID: ")
    contraseña = input("Contraseña: ")
    for u in usuarios:
        if u["id"] == id_usuario and u["contraseña"] == contraseña:
            usuarios.remove(u)
            print("Usuario eliminado.")
            return
    print("ID o contraseña incorrectos.")

def acceso_rectorado():
    print("Bienvenido a la biblioteca del rectorado.")
    mostrar_libros(universidad["Rectorado"]["biblioteca"])

def mostrar_libros(lista):
    for libro in lista:
        estado = "Disponible" if libro["disponible"] else "No disponible"
        print(f"{libro['titulo']} - {libro['autor']} ({libro['año']}) - {estado}")

def acceso_campus():
    entrada = input("¿A qué campus quieres acceder?: ")
    campus = normalizar_campus(entrada)
    if campus in universidad:
        print(f"Mostrando biblioteca general del campus {campus}:")
        mostrar_libros(universidad[campus]["biblioteca"])
    else:
        print("Campus no válido.")

def acceso_carrera():
    id_usuario = input("ID de usuario: ")
    contraseña = input("Contraseña: ")
    for u in usuarios:
        if u["id"] == id_usuario and u["contraseña"] == contraseña:
            campus = u["campus"]
            print(f"Acceso concedido a la biblioteca de {u['carrera']} en campus {campus}.")
            libros = universidad.get(campus, {}).get("biblioteca", [])
            mostrar_libros([l for l in libros if random.choice([True, False])])
            return
    print("ID o contraseña incorrectos.")

def buscar_libro():
    criterio = input("Buscar por (titulo/autor/año): ").lower()
    valor = input("Valor a buscar: ").lower()
    for campus in universidad:
        for libro in universidad[campus]["biblioteca"]:
            if libro[criterio].lower() == valor:
                estado = "Disponible" if libro["disponible"] else "No disponible"
                print(f"{libro['titulo']} - {libro['autor']} ({libro['año']}) - {estado}")

def reservar_libro():
    id_usuario = input("Tu ID: ")
    for u in usuarios:
        if u["id"] == id_usuario:
            libros_usuario = reservas.get(id_usuario, [])
            if len(libros_usuario) >= 3:
                print("Ya tienes 3 libros reservados.")
                return
            titulo = input("Título del libro a reservar: ").lower()
            for libro in universidad[u["campus"]]["biblioteca"]:
                if libro["titulo"].lower() == titulo and libro["disponible"]:
                    libro["disponible"] = False
                    libros_usuario.append((libro, 4))
                    reservas[id_usuario] = libros_usuario
                    print("Libro reservado.")
                    return
            print("Libro no encontrado o no disponible.")
            return
    print("ID no válido.")

def mostrar_reservas():
    id_usuario = input("Tu ID: ")
    if id_usuario in reservas:
        for libro, dias in reservas[id_usuario]:
            print(f"{libro['titulo']} - {libro['autor']} ({libro['año']}) - {dias} días restantes")
    else:
        print("No tienes libros reservados.")

def devolver_libro():
    id_usuario = input("Tu ID: ")
    if id_usuario in reservas:
        titulo = input("Título del libro a devolver: ").lower()
        libros = reservas[id_usuario]
        for libro, dias in libros:
            if libro["titulo"].lower() == titulo:
                libro["disponible"] = True
                libros.remove((libro, dias))
                print("Libro devuelto.")
                return
        print("Libro no encontrado entre tus reservas.")
    else:
        print("No tienes libros reservados.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Darse de alta")
        print("2. Darse de baja")
        print("3. Acceder a biblioteca del rectorado")
        print("4. Acceder a biblioteca general de campus")
        print("5. Acceder a biblioteca de carrera")
        print("6. Mostrar libros de la biblioteca actual")
        print("7. Buscar libro")
        print("8. Reservar libro")
        print("9. Ver reservas")
        print("10. Devolver libro")
        print("11. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            baja_usuario()
        elif opcion == "3":
            acceso_rectorado()
        elif opcion == "4":
            acceso_campus()
        elif opcion == "5":
            acceso_carrera()
        elif opcion == "6":
            acceso_campus()
        elif opcion == "7":
            buscar_libro()
        elif opcion == "8":
            reservar_libro()
        elif opcion == "9":
            mostrar_reservas()
        elif opcion == "10":
            devolver_libro()
        elif opcion == "11":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Iniciar el menú
menu()
