import tkinter as tk
from tkinter import messagebox

# Definimos la ventana principal
def ventana_principal():
    global v_principal
    v_principal = tk.Tk()
    v_principal.title("Calculadora")
    v_principal.geometry("500x300")

    #Creamos menú
    menu_bar = tk.Menu(v_principal)
    v_principal.config(menu=menu_bar)

    #Añadimos una barra de menú
    menu_mod_password = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Modificar contraseña", menu=menu_mod_password)
    
    #Añadimos el menú "Inicio"
    menu_inicio = tk.Menu(menu_bar, tearoff=0)
    menu_inicio.add_cascade(label="Inicio", command=return_login)
    menu_bar.add_cascade(label="Inicio", menu=menu_inicio)

    v_principal.mainloop()

def validate_password():
    with open('.//persistencia.txt', 'r') as file:
        history_password = file.read().strip()

    if password_entry.get() == history_password:
        login.destroy()
        ventana_principal()
    else:
        messagebox.showerror("Error", "Error de contraseña")

def return_login():
    v_principal.destroy()
    ventana_login()

def salir():
    login.destroy()

def ventana_login():
    global login, password_entry
    login = tk.Tk()
    login.title("cal")
    login.geometry("500x300")
    login.configure(bg="white")

    #etiqueta para agregar contraseña
    password_label = tk.Label(login, text="Contraseña:", bg="white")
    password_label.pack()
    password_entry = tk.Entry(login, show="*")
    password_entry.pack(pady=5)

    #botón de inicio de sesión
    login_button = tk.Button(login, text="Iniciar sesión", command=validate_password, bg="white")
    login_button.pack()
    
    #botón de salir
    salir_button = tk.Button(login, text="x", foreground="red", bg = "white", command=salir)
    salir_button.place(x=470, y=270)

    login.mainloop()

#Iniciamos la ventana de login
ventana_login()
