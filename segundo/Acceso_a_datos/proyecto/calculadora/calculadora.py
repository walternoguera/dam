'''
Programa calculadora
(c) 2025 Walter Morel
v0.1
'''
import tkinter
from tkinter import messagebox
import math

contrasena_global = "1234"

def ventana_principal():
    ventana = tkinter.Tk()
    ventana.geometry("+480+180")
    ventana.configure(bg="white")
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    def regresar_a_login():
        ventana.destroy()
        ventana_login()

    #definimos el menú
    menu_bar = tkinter.Menu(ventana)
    menu_bar.add_command(label="> Regresar a Login", command=regresar_a_login)
    ventana.config(menu=menu_bar)

    #funciones
    def sumar():
        try:
            valor1 = entrada_valor1.get()
            valor2 = entrada_valor2.get()
            if valor1 == "" or valor2 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Faltan valores para sumar")
                messagebox.showwarning("Error", "Faltan valores para sumar")
            else:
                resultado = int(valor1) + int(valor2)
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valores no válidos")

    def restar():
        try:
            valor1 = entrada_valor1.get()
            valor2 = entrada_valor2.get()
            if valor1 == "" or valor2 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Faltan valores para restar")
                messagebox.showwarning("Error", "Faltan valores para restar")
            else:
                resultado = int(valor1) - int(valor2)
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valores no válidos")

    def multiplicar():
        try:
            valor1 = entrada_valor1.get()
            valor2 = entrada_valor2.get()
            if valor1 == "" or valor2 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Faltan valores para multiplicar")
                messagebox.showwarning("Error", "Faltan valores para multiplicar")
            else:
                resultado = int(valor1) * int(valor2)
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valores no válidos")

    def dividir():
        try:
            valor1 = entrada_valor1.get()
            valor2 = entrada_valor2.get()
            if valor1 == "" or valor2 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Faltan valores para dividir")
                messagebox.showwarning("Error", "Faltan valores para dividir")
            else:
                if int(valor2) == 0:
                    resultado_text.delete(0, tkinter.END)
                    resultado_text.insert(0, "No se puede dividir por 0")
                    messagebox.showerror("Error", "No se puede dividir por 0")
                else:
                    resultado = int(valor1) / int(valor2)
                    resultado_text.delete(0, tkinter.END)
                    resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valores no válidos")

    def absoluto():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular el absoluto")
                messagebox.showwarning("Error", "Falta un valor para calcular el absoluto")
            else:
                resultado = abs(int(valor1))
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def seno():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular el seno")
                messagebox.showwarning("Error", "Falta un valor para calcular el seno")
            else:
                resultado = math.sin(math.radians(float(valor1)))
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def coseno():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular el coseno")
                messagebox.showwarning("Error", "Falta un valor para calcular el coseno")
            else:
                resultado = math.cos(math.radians(float(valor1))) 
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def tangente():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular la tangente")
                messagebox.showwarning("Error", "Falta un valor para calcular la tangente")
            else:
                resultado = math.tan(math.radians(float(valor1))) 
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def logaritmo_base10():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular el logaritmo base 10")
                messagebox.showwarning("Error", "Falta un valor para calcular el logaritmo base 10")
            else:
                resultado = math.log10(float(valor1)) 
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def logaritmo_neperiano():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular el logaritmo neperiano")
                messagebox.showwarning("Error", "Falta un valor para calcular el logaritmo neperiano")
            else:
                resultado = math.log(float(valor1))  # Cálculo del logaritmo neperiano
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def exponente():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular e^x")
                messagebox.showwarning("Error", "Falta un valor para calcular e^x")
            else:
                resultado = math.exp(float(valor1)) 
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def raiz_cuadrada():
        try:
            valor1 = entrada_valor1.get()
            if valor1 == "":
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, "Falta un valor para calcular la raíz cuadrada")
                messagebox.showwarning("Error", "Falta un valor para calcular la raíz cuadrada")
            else:
                resultado = math.sqrt(float(valor1)) 
                resultado_text.delete(0, tkinter.END)
                resultado_text.insert(0, resultado)
        except:
            messagebox.showerror("Error de parametros", "Error, valor no válido")

    def nuevo():
        entrada_valor1.delete(0, tkinter.END)
        entrada_valor2.delete(0, tkinter.END)
        resultado_text.delete(0, tkinter.END)

    #Título de la app
    label_titulo = tkinter.Label(ventana, text="Calculadora", font="arial 20", bg="white")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=8)

    #Valor 1
    label_valor1 = tkinter.Label(ventana, text="NÚMERO 1", font="arial 10", bg="white")
    label_valor1.grid(row=1, column=0, pady=5)
    entrada_valor1 = tkinter.Entry(ventana, font="arial 10", bg="white")
    entrada_valor1.grid(row=1, column=1, padx=8)

    #Valor 2
    label_valor2 = tkinter.Label(ventana, text="NÚMERO 2", font="arial 10", bg="white")
    label_valor2.grid(row=2, column=0, pady=5)
    entrada_valor2 = tkinter.Entry(ventana, font="arial 10", bg="white")
    entrada_valor2.grid(row=2, column=1, padx=8)

    #Resultado
    label_resultado = tkinter.Label(ventana, text="RESULTADO", font="arial 10", bg="white")
    label_resultado.grid(row=3, column=0, pady=5)
    resultado_text = tkinter.Entry(ventana, font="arial 10")
    resultado_text.grid(row=3, column=1, padx=8)

    #Botones 
    boton_suma = tkinter.Button(ventana, text="Suma", bg="lightgreen", fg="black", font="arial 12", width=15, command=sumar)
    boton_suma.grid(row=4, column=0, pady=1)
    boton_suma.grid(row=4, column=0, padx=7)

    boton_resta = tkinter.Button(ventana, text="Resta", bg="lightblue", fg="black", font="arial 12", width=15, command=restar)
    boton_resta.grid(row=4, column=1, pady=2)

    boton_mult = tkinter.Button(ventana, text="Multiplicación", bg="lightyellow", fg="black", font="arial 12", width=15, command=multiplicar)
    boton_mult.grid(row=5, column=0, pady=2)

    boton_div = tkinter.Button(ventana, text="División", bg="orange", fg="black", font="arial 12", width=15, command=dividir)
    boton_div.grid(row=5, column=1, pady=2)

    boton_abs = tkinter.Button(ventana, text="Valor Absoluto", bg="purple", fg="white", font="arial 12", width=15, command=absoluto)
    boton_abs.grid(row=6, column=0, pady=2)

    boton_seno = tkinter.Button(ventana, text="Seno", bg="lightpink", fg="black", font="arial 12", width=15, command=seno)
    boton_seno.grid(row=6, column=1, pady=2)

    boton_coseno = tkinter.Button(ventana, text="Coseno", bg="cyan", fg="black", font="arial 12", width=15, command=coseno)
    boton_coseno.grid(row=7, column=0, pady=2)

    boton_tangente = tkinter.Button(ventana, text="Tangente", bg="salmon", fg="black", font="arial 12", width=15, command=tangente)
    boton_tangente.grid(row=7, column=1, pady=2)

    boton_log10 = tkinter.Button(ventana, text="Log. Base 10", bg="gold", fg="black", font="arial 12", width=15, command=logaritmo_base10)
    boton_log10.grid(row=8, column=0, pady=2)

    boton_ln = tkinter.Button(ventana, text="Log. Neperiano", bg="lightcoral", fg="black", font="arial 12", width=15, command=logaritmo_neperiano)
    boton_ln.grid(row=8, column=1, pady=2)

    boton_exp = tkinter.Button(ventana, text="e^x", bg="mediumseagreen", fg="black", font="arial 12", width=15, command=exponente)
    boton_exp.grid(row=9, column=0, pady=2)

    boton_sqrt = tkinter.Button(ventana, text="Raíz Cuadrada", bg="plum", fg="black", font="arial 12", width=15, command=raiz_cuadrada)
    boton_sqrt.grid(row=9, column=1, pady=2)


    boton_nuevo = tkinter.Button(ventana, text="Nuevo", bg="red", fg="white", font="arial 12", width=15, command=nuevo)
    boton_nuevo.grid(row=10, column=0, columnspan=2, pady=5)

    ventana.mainloop()

def ventana_login():
    global contrasena_global

    def cambiar_contrasena():
        def guardar_contrasena():
            nueva_contrasena = entrada_nueva_contrasena.get()
            if nueva_contrasena:
                global contrasena_global
                contrasena_global = nueva_contrasena
                messagebox.showinfo("Éxito", "Contraseña cambiada exitosamente")
                ventana_cambiar.destroy()
            else:
                messagebox.showerror("Error", "La contraseña no puede estar vacía")

        ventana_cambiar = tkinter.Toplevel()
        ventana_cambiar.geometry("+480+180")
        ventana_cambiar.title("Cambiar Contraseña")
        ventana_cambiar.configure(bg="white")

        label_nueva_contrasena = tkinter.Label(ventana_cambiar, text="Contraseña nueva:", font="arial 15", bg="white")
        label_nueva_contrasena.grid(row=0, column=0, pady=5)
        entrada_nueva_contrasena = tkinter.Entry(ventana_cambiar, font="arial 15", show="*")
        entrada_nueva_contrasena.grid(row=0, column=1, padx=8)

        boton_guardar = tkinter.Button(ventana_cambiar, text="Guardar", bg="green", fg="white", font="arial 12", command=guardar_contrasena)
        boton_guardar.grid(row=1, column=0, columnspan=2, pady=10)

    def verificar_contrasena():
        if entrada_contrasena.get() == contrasena_global:
            login.destroy()
            ventana_principal()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    login = tkinter.Tk()
    login.geometry("+480+180")
    login.columnconfigure(0, weight=1)
    login.columnconfigure(1, weight=1)
    login.configure(bg="white")

    label_titulo = tkinter.Label(login, text="Inicio de Sesión", font="arial 20", bg="white")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=8)

    label_contrasena = tkinter.Label(login, text="Contraseña:", font="arial 15", bg="white")
    label_contrasena.grid(row=1, column=0, pady=5)
    entrada_contrasena = tkinter.Entry(login, font="arial 15", show="*")
    entrada_contrasena.grid(row=1, column=1, padx=8)

    boton_entrar = tkinter.Button(login, text="Entrar", bg="black", fg="white", font="arial 12", width=10, command=verificar_contrasena)
    boton_entrar.grid(row=2, column=0, pady=5)

    boton_cambiar = tkinter.Button(login, text="Cambiar Contraseña", bg="blue", fg="white", font="arial 12", width=20, command=cambiar_contrasena)
    boton_cambiar.grid(row=2, column=1, pady=5)

    login.mainloop()

ventana_login()
