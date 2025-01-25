import tkinter as tk
from tkinter import messagebox

# Variable para almacenar la contraseña
password = "1234"  # Cambia "1234" por la contraseña que desees

def validate_password():
    if password_entry.get() == password:
        login.destroy()
        ventana_principal()
    else:
        messagebox.showerror("Error", "Error de contraseña")

def return_login():
    v_principal.destroy()
    ventana_login()

def salir():
    login.destroy()

def sumar(numero1_entry, numero2_entry, resultado_entry):
    try:
        numero1 = float(numero1_entry.get())
        numero2 = float(numero2_entry.get())
        resultado = numero1 + numero2
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, str(resultado))
        resultado_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def restar(numero1_entry, numero2_entry, resultado_entry):
    try:
        numero1 = float(numero1_entry.get())
        numero2 = float(numero2_entry.get())
        resultado = numero1 - numero2
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, str(resultado))
        resultado_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def multiplicar(numero1_entry, numero2_entry, resultado_entry):
    try:
        numero1 = float(numero1_entry.get())
        numero2 = float(numero2_entry.get())
        resultado = numero1 * numero2
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, str(resultado))
        resultado_entry.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def dividir(numero1_entry, numero2_entry, resultado_entry):
    try:
        numero1 = float(numero1_entry.get())
        numero2 = float(numero2_entry.get())
        if numero2 == 0:
            raise ZeroDivisionError
        resultado = numero1 / numero2
        resultado_entry.config(state="normal")
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, str(resultado))
        resultado_entry.config(state="readonly")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def limpiar(numero1_entry, numero2_entry, resultado_entry):
    numero1_entry.delete(0, tk.END)
    numero2_entry.delete(0, tk.END)
    resultado_entry.config(state="normal")
    resultado_entry.delete(0, tk.END)
    resultado_entry.config(state="readonly")

def ventana_principal():
    global v_principal
    v_principal = tk.Tk()
    v_principal.title("Calculadora")
    v_principal.geometry("500x300")

    # Creamos menú
    menu_bar = tk.Menu(v_principal)
    v_principal.config(menu=menu_bar)

    menu_mod_password = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Modificar contraseña", menu=menu_mod_password)
    
    menu_inicio = tk.Menu(menu_bar, tearoff=0)
    menu_inicio.add_cascade(label="Inicio", command=return_login)
    menu_bar.add_cascade(label="Inicio", menu=menu_inicio)

    # Marco para organizar las entradas
    frame = tk.Frame(v_principal)
    frame.pack(pady=10)

    # Cajas de texto lado a lado
    tk.Label(frame, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
    numero1_entry = tk.Entry(frame)
    numero1_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Número 2:").grid(row=0, column=2, padx=5, pady=5)
    numero2_entry = tk.Entry(frame)
    numero2_entry.grid(row=0, column=3, padx=5, pady=5)

    # Caja de resultado
    tk.Label(v_principal, text="Resultado:").pack()
    resultado_entry = tk.Entry(v_principal, state="readonly")
    resultado_entry.pack(pady=5)

    # Botones
    button_frame = tk.Frame(v_principal)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Sumar", command=lambda: sumar(numero1_entry, numero2_entry, resultado_entry)).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Restar", command=lambda: restar(numero1_entry, numero2_entry, resultado_entry)).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Multiplicar", command=lambda: multiplicar(numero1_entry, numero2_entry, resultado_entry)).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Dividir", command=lambda: dividir(numero1_entry, numero2_entry, resultado_entry)).grid(row=0, column=3, padx=5)

    limpiar_button = tk.Button(v_principal, text="Limpiar", command=lambda: limpiar(numero1_entry, numero2_entry, resultado_entry))
    limpiar_button.place(x=420, y=270)

    v_principal.mainloop()

def ventana_login():
    global login, password_entry
    login = tk.Tk()
    login.title("cal")
    login.geometry("500x300")
    login.configure(bg="white")

    # Etiqueta para agregar contraseña
    password_label = tk.Label(login, text="Contraseña:", bg="white")
    password_label.pack()
    password_entry = tk.Entry(login, show="*")
    password_entry.pack(pady=5)

    # Botón de inicio de sesión
    login_button = tk.Button(login, text="Iniciar sesión", command=validate_password, bg="white")
    login_button.pack()
    
    # Botón de salir
    salir_button = tk.Button(login, text="x", foreground="red", bg="white", command=salir)
    salir_button.place(x=470, y=270)

    login.mainloop()

# Iniciamos la ventana de login
ventana_login()
