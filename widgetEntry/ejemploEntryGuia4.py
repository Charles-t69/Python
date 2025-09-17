import tkinter as tk
from tkinter import *

# Crear la ventana principal
root = Tk()
root.title("Formulario - Tu Nombre Aquí")   # Cambia "Tu Nombre Aquí" por el tuyo
# root.iconbitmap("icono.ico")                # Coloca un archivo .ico en la misma carpeta

# Crear un frame para organizar los elementos
miFrame = Frame(root, width=400, height=300)
miFrame.pack()

# ===================== Labels ======================
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")

apellidoLabel = Label(miFrame, text="Apellidos:")
apellidoLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

correoLabel = Label(miFrame, text="Correo Electrónico:")
correoLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")

# ===================== Entrys ======================
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroCorreo = Entry(miFrame)
cuadroCorreo.grid(row=2, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, show="*")  # Ocultar caracteres con "*"
cuadroPass.grid(row=3, column=1, padx=10, pady=10)

# ===================== Botón ======================
def enviar():
    print("Nombre:", cuadroNombre.get())
    print("Apellidos:", cuadroApellido.get())
    print("Correo:", cuadroCorreo.get())
    print("Contraseña:", cuadroPass.get())

botonEnviar = Button(root, text="Enviar", command=enviar)
botonEnviar.pack(pady=10)

# Mantener la ventana abierta
root.mainloop()
