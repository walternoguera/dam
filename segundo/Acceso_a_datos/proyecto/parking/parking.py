import tkinter
import random
from tkinter import messagebox

NUM_PLAZAS = 200

#Número de coches (aleatorio entre 196 y 200)
coches_actuales = random.randint(196, 200)

def actualizar_estado(label_estado):
    label_estado.config(text=f"Plazas ocupadas: {coches_actuales}/{NUM_PLAZAS}")

def aparcar(label_estado):
    global coches_actuales
    if coches_actuales < NUM_PLAZAS:
        coches_actuales += 1
        actualizar_estado(label_estado)
    else:
        messagebox.showwarning("Parking lleno", "No hay plazas disponibles")

def retirar(label_estado):
    global coches_actuales
    if coches_actuales > 0:
        coches_actuales -= 1
        actualizar_estado(label_estado)
    else:
        messagebox.showwarning("Parking vacío", "No hay coches en el parking para retirar.")

def resetear_parking(label_estado):
    global coches_actuales
    coches_actuales = random.randint(196, 200)  #Reiniciamos el número de coches
    actualizar_estado(label_estado)

def main():
    global coches_actuales

    #Ventana principal
    ventana = tkinter.Tk()
    ventana.geometry("400x250")
    ventana.title("Gestión de Parking")

    #Etiqueta de título
    label_titulo = tkinter.Label(ventana, text="Gestión de Parking", font=("Arial", 16))
    label_titulo.pack(pady=10)

    label_estado = tkinter.Label(ventana, text=f"Plazas ocupadas: {coches_actuales}/{NUM_PLAZAS}", font=("Arial", 12))
    label_estado.pack(pady=10)

    #botones
    def aparcar_evento():
        aparcar(label_estado)

    boton_aparcar = tkinter.Button(ventana, text="Aparcar", bg="lightgreen", font=("Arial", 12), command=aparcar_evento)
    boton_aparcar.pack(side="left", padx=20, pady=20)

    def retirar_evento():
        retirar(label_estado)

    boton_retirar = tkinter.Button(ventana, text="Retirar", bg="lightblue", font=("Arial", 12), command=retirar_evento)
    boton_retirar.pack(side="right", padx=20, pady=20)

    def reiniciar_evento():
        resetear_parking(label_estado)

    boton_reset = tkinter.Button(ventana, text="Empezar de nuevo", bg="orange", font=("Arial", 12), command=reiniciar_evento)
    boton_reset.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
