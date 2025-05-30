# === IMPORTS Y CONFIGURACIÓN INICIAL ===
import random
import datetime

# === MULTILENGUAJE ===
idiomas = {
    'es': {
        'menu': "-- MENÚ PRINCIPAL --",
        'alta': "Alta usuario",
        'reservar': "Reservar libro",
        'devolver': "Devolver libro",
        'buscar': "Buscar avanzado",
        'recomendar': "Ver recomendaciones",
        'recordatorio': "Ver recordatorios",
        'admin': "Login admin",
        'salir': "Salir",
        'admin_panel': "-- PANEL DE ADMINISTRADOR --",
        'admin_historial': "Ver historial de todos los estudiantes",
        'admin_add': "Añadir libro",
        'admin_lang': "Cambiar idioma",
        'admin_back': "Volver"
    },
    'en': {
        'menu': "-- MAIN MENU --",
        'alta': "Register user",
        'reservar': "Reserve book",
        'devolver': "Return book",
        'buscar': "Advanced search",
        'recomendar': "View recommendations",
        'recordatorio': "View reminders",
        'admin': "Admin login",
        'salir': "Exit",
        'admin_panel': "-- ADMIN PANEL --",
        'admin_historial': "View all students' history",
        'admin_add': "Add book",
        'admin_lang': "Change language",
        'admin_back': "Back"
    }
}
lang = 'es'

# === NORMALIZACIÓN DE CAMPUS ===
def normalizar_campus(entrada):
    equivalencias = {
        "ciencia": "Ciencia",
        "tecnologia": "Tecnología",
        "tecnología": "Tecnología",
        "sanitario": "Sanitario",
        "legal": "Legal"
    }
    return equivalencias.get(entrada.strip().lower(), None)

# === BASE DE DATOS SIMULADA ===
universidad = {
    "Ciencia": {"carreras": ["Biología", "Química", "Física", "Matemáticas", "Geología"], "biblioteca": []},
    "Tecnología": {"carreras": ["Informática", "Ingeniería", "Robótica", "Telecomunicaciones", "Sistemas"], "biblioteca": []},
    "Sanitario": {"carreras": ["Enfermería", "Medicina", "Fisioterapia", "Farmacia", "Odontología"], "biblioteca": []},
    "Legal": {"carreras": ["Derecho", "Criminología", "Relaciones Laborales", "Administración Pública", "Política"], "biblioteca": []},
    "Rectorado": {"carreras": [], "biblioteca": []}
}

usuarios = []
reservas = {}
historial = {}
sanciones = {}

# === FUNCIONES DE LIBROS ===
def crear_libro(titulo, autor, año, genero):
    return {"titulo": titulo, "autor": autor, "año": año, "genero": genero, "disponible": True}

libros_demo = [
    crear_libro("Python Básico", "Laura Díaz", "2018", "Programación"),
    crear_libro("Física Cuántica", "Luis Torres", "2015", "Ciencia"),
    crear_libro("Derecho Penal", "Gabriela Ruiz", "2010", "Legal"),
    crear_libro("Historia del Arte", "Manuel Pérez", "2005", "Arte")
]

for campus in universidad:
    universidad[campus]["biblioteca"] = libros_demo.copy()

# === FUNCIONES DE USUARIO ===
def registrar_usuario():
    nombre = input("Nombre del estudiante: ")
    campus = normalizar_campus(input("Campus: "))
    if campus is None:
        print("Campus no válido.")
        return
    carrera = input("Carrera: ")
    contraseña = input("Contraseña: ")
    id_usuario = f"{nombre}_{random.randint(100,999)}"
    usuarios.append({"id": id_usuario, "nombre": nombre, "campus": campus, "carrera": carrera, "contraseña": contraseña})
    print(f"Registrado con ID: {id_usuario}")

def ver_mi_historial():
    uid = input("Tu ID: ")
    if uid in historial:
        print(f"Historial de {uid}:")
        for item in historial[uid]:
            print(item)
    else:
        print("No hay historial registrado.")

# === SECCIÓN ADMIN ===
def login_admin():
    usuario = input("Usuario admin: ")
    clave = input("Contraseña: ")
    if usuario == "admin" and clave == "admin123":
        menu_admin()
    else:
        print("Acceso denegado.")

def menu_admin():
    while True:
        print(f"\n{idiomas[lang]['admin_panel']}")
        print(f"1. {idiomas[lang]['admin_historial']}")
        print(f"2. {idiomas[lang]['admin_add']}")
        print(f"3. {idiomas[lang]['admin_lang']}")
        print(f"4. {idiomas[lang]['admin_back']}")
        op = input("Opción: ")
        if op == "1":
            for uid, prestamos in historial.items():
                print(f"Historial de {uid}:")
                for item in prestamos:
                    print(item)
        elif op == "2":
            agregar_libro()
        elif op == "3":
            cambiar_idioma()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

def cambiar_idioma():
    global lang
    nuevo = input("Idioma (es/en): ").lower()
    if nuevo in idiomas:
        lang = nuevo
        print(f"Idioma cambiado a {nuevo}")
    else:
        print("Idioma no válido.")

def agregar_libro():
    campus = normalizar_campus(input("Campus destino: "))
    if campus in universidad:
        titulo = input("Título: ")
        autor = input("Autor: ")
        año = input("Año: ")
        genero = input("Género: ")
        libro = crear_libro(titulo, autor, año, genero)
        universidad[campus]["biblioteca"].append(libro)
        print("Libro añadido.")
    else:
        print("Campus no válido.")

# === FUNCIONES DE RESERVA, HISTORIAL Y SANCIONES ===
def reservar_libro():
    uid = input("Tu ID: ")
    if sanciones.get(uid):
        print("Tienes sanciones activas. No puedes reservar libros.")
        return
    titulo = input("Título a reservar: ").lower()
    for campus in universidad:
        for libro in universidad[campus]["biblioteca"]:
            if libro["titulo"].lower() == titulo and libro["disponible"]:
                libro["disponible"] = False
                fecha = datetime.date.today() - datetime.timedelta(days=4)
                reservas.setdefault(uid, []).append((libro, fecha))
                historial.setdefault(uid, []).append(f"{libro['titulo']} prestado el {fecha}")
                print("Libro reservado.")
                return
    print("Libro no encontrado o no disponible.")

def devolver_libro():
    uid = input("Tu ID: ")
    titulo = input("Título a devolver: ").lower()
    if uid in reservas:
        nuevos = []
        for libro, fecha in reservas[uid]:
            if libro["titulo"].lower() == titulo:
                libro["disponible"] = True
                fecha_dev = datetime.date.today()
                historial[uid].append(f"{libro['titulo']} devuelto el {fecha_dev}")
                if (fecha_dev - fecha).days > 4:
                    sanciones[uid] = True
                    print("Libro devuelto con retraso. Se ha aplicado una sanción.")
            else:
                nuevos.append((libro, fecha))
        reservas[uid] = nuevos

# === FUNCIONES DE BÚSQUEDA Y RECOMENDACIONES ===
def buscar_avanzado():
    autor = input("Autor: ").lower()
    genero = input("Género: ").lower()
    año = input("Año (opcional): ").strip()
    resultados = []
    for campus in universidad:
        for libro in universidad[campus]["biblioteca"]:
            if autor in libro["autor"].lower() and genero in libro["genero"].lower():
                if año == "" or libro["año"] == año:
                    resultados.append(libro)
    resultados = sorted(resultados, key=lambda x: x["titulo"])
    for libro in resultados:
        print(f"{libro['titulo']} - {libro['autor']} ({libro['año']}) - {libro['genero']}")

def recomendaciones(uid):
    print("Recomendaciones basadas en tu historial:")
    if uid in historial:
        temas = [l.split()[0].lower() for l in historial[uid]]
        for campus in universidad:
            for libro in universidad[campus]["biblioteca"]:
                if libro["titulo"].split()[0].lower() in temas:
                    print(f"- {libro['titulo']} ({libro['genero']})")

# === NOTIFICACIONES Y RECORDATORIOS ===
def enviar_recordatorios():
    hoy = datetime.date.today()
    encontrado = False
    for uid, libros in reservas.items():
        for libro, fecha in libros:
            dias = (hoy - fecha).days
            if dias >= 3:
                print(f"Recordatorio para {uid}: devuelve '{libro['titulo']}' pronto. (Prestado hace {dias} días)")
                encontrado = True
    if not encontrado:
        print("No hay recordatorios pendientes.")

# === MENÚ PRINCIPAL ===
def menu():
    while True:
        print(f"\n{idiomas[lang]['menu']}")
        print(f"1. {idiomas[lang]['alta']}")
        print(f"2. {idiomas[lang]['reservar']}")
        print(f"3. {idiomas[lang]['devolver']}")
        print(f"4. {idiomas[lang]['buscar']}")
        print(f"5. {idiomas[lang]['recomendar']}")
        print(f"6. {idiomas[lang]['recordatorio']}")
        print(f"7. {idiomas[lang]['admin']}")
        print(f"8. Ver mi historial")
        print(f"9. {idiomas[lang]['salir']}")
        op = input("Opción: ")
        if op == "1":
            registrar_usuario()
        elif op == "2":
            reservar_libro()
        elif op == "3":
            devolver_libro()
        elif op == "4":
            buscar_avanzado()
        elif op == "5":
            uid = input("Tu ID: ")
            recomendaciones(uid)
        elif op == "6":
            enviar_recordatorios()
        elif op == "7":
            login_admin()
        elif op == "8":
            ver_mi_historial()
        elif op == "9":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")

# === INICIO ===
menu()
