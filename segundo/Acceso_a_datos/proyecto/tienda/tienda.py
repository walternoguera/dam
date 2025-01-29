# Listas principales
productos = []
carrito = []
historial = []


def iniciar_sesion():
    while True:
        print(bcolors.HEADER + "\n--- Bienvenido a la tienda virtual ---"+ bcolors.ENDC)
        print("1. Cliente")
        print("2. Vendedor")
        print("3. Salir")
        opcion = input("Selecciona tu perfil (1 o 2): ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            password = input("Introduce la contraseña de vendedor: ")
            if password == "1234":
                menu_vendedor()
            else:
                print("Contraseña incorrecta. Intenta de nuevo.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

#Menú del Cliente
def menu_cliente():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Cancelar compra")
        print("6. Cerrar sesión")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            comprar_productos()
            return  #Regresar al login
        elif opcion == "5":
            cancelar_compra()
            return  #Regresar al login 
        elif opcion == "6":
            print("Cerrando sesión...")
            return  #Regresar al login
        else:
            print("Opción inválida, intenta de nuevo.")

def menu_vendedor():
    while True:
        print("\n--- Menú Vendedor ---")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Modificar precio o cantidad")
        print("4. Eliminar producto")
        print("5. Cerrar sesión")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            modificar_precio()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Cerrando sesión...")
            return  #Regresar al login
        else:
            print("Opción inválida, intenta de nuevo.")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mostrar_productos():
    if not productos:
        print("No hay productos disponibles en la tienda.")
    else:
        print("\n--- Productos Disponibles ---")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Cantidad: {p[2]}, Precio: {p[3]}€")

def agregar_producto():
    if len(productos) >= 8:
        print("La tienda ya tiene el máximo de 8 productos.")
        return

    id_producto = len(historial) + 1  #generar id unico
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad: "))
    precio = float(input("Introduce el precio: "))

    if cantidad < 0 or precio < 0:
        print("La cantidad y el precio deben ser valores positivos.")
        return

    for producto in productos:
        if producto[1].lower() == nombre.lower():
            producto[2] += cantidad
            producto[3] = precio
            print(f"Producto {nombre} actualizado con éxito.")
            return

    productos.append([id_producto, nombre, cantidad, precio])
    print(f"Producto {nombre} agregado correctamente.")

#Modificar el precio o cantidad de un producto (solo vendedor)
def modificar_precio():
    nombre = input("Introduce el nombre del producto a modificar: ")
    for producto in productos:
        if producto[1].lower() == nombre.lower():
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            if nuevo_precio < 0 or nueva_cantidad < 0:
                print("El precio y la cantidad deben ser valores positivos.")
                return

            producto[3] = nuevo_precio
            producto[2] = nueva_cantidad
            print(f"Producto {nombre} modificado con éxito.")
            return

    print("Producto no encontrado.")

#Eliminar un producto (manteniendo su historial)
def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for p in productos:
        if p[1].lower() == nombre.lower():
            historial.append([p[0], p[1], [p[3]]])  # Guardar en historial
            productos.remove(p)
            print(f"Producto {nombre} eliminado correctamente.")
            return

    print("Producto no encontrado.")

#Agregar un producto al carrito (para clientes)
def agregar_al_carrito():
    nombre = input("Introduce el nombre del producto que quieres comprar: ")
    cantidad = int(input("Introduce la cantidad: "))

    for p in productos:
        if p[1].lower() == nombre.lower():
            if p[2] >= cantidad:
                p[2] -= cantidad
                carrito.append([p[1], cantidad, p[3]])
                print(f"{cantidad} unidades de {p[1]} añadidas al carrito.")
                return
            else:
                print("No hay suficiente stock disponible.")
                return

    print(bcolors.WARNING+"Producto no encontrado."+ bcolors.ENDC)

#Ver el carrito del cliente
def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        total = 0
        print("\n--- Carrito de Compras ---")
        for c in carrito:
            print(f"Producto: {c[0]}, Cantidad: {c[1]}, Precio Unitario: {c[2]}€, Subtotal: {c[1] * c[2]}€")
            total += c[1] * c[2]
        print(f"Total: {total}€")

#Finalizar la compra y vaciar el carrito
def comprar_productos():
    if not carrito:
        print("No hay productos en el carrito.")
        return

    total = sum(c[1] * c[2] for c in carrito)
    print(f"Compra finalizada. Total a pagar: {total}€")
    print("Gracias por tu compra.")

    carrito.clear()
    print("\nVolviendo al inicio de sesión...\n")

#Cancelar la compra y devolver productos al inventario
def cancelar_compra():
    if not carrito:
        print("El carrito ya está vacío.")
        return

    for c in carrito:
        for p in productos:
            if p[1] == c[0]:
                p[2] += c[1]

    carrito.clear()
    print("Compra cancelada. Los productos han sido devueltos al inventario.")
    print("\nVolviendo al inicio de sesión...\n")

#Iniciar la aplicación
if __name__ == "__main__":
    iniciar_sesion()
