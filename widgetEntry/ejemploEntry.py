from tkinter import *

raiz = Tk()
raiz.title("Formulario de Registro - Por Daniel Veloza") 

try:
    raiz.iconbitmap("social.ico")  # Asegúrate de tener este archivo
except:
    print("Icono no encontrado. Continuaremos sin él...")

miFrame = Frame(raiz)
miFrame.pack(padx=20, pady=20)
miFrame.config(bg="cyan")  


minombre = StringVar()

def codigoBoton():
    minombre.set("----")  

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellidos:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=10)

# (Guía 4)
passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*") 

# (Guía 5)
comentLabel = Label(miFrame, text="Comentarios:")
comentLabel.grid(row=4, column=0, sticky="ne", padx=10, pady=10) 

# (Guía 5)
cuadroComent = Text(miFrame, width=15, height=5)
cuadroComent.grid(row=4, column=1, padx=10, pady=10)

scrollComent = Scrollbar(miFrame, command=cuadroComent.yview)
scrollComent.grid(row=4, column=2, sticky="nsew")

cuadroComent.config(yscrollcommand=scrollComent.set)

# (Guía 5)
botonEnviar = Button(raiz, text="Enviar", command=codigoBoton)
botonEnviar.pack(pady=10)

# Cambiar Label de Dirección por Correo Electrónico 
direccionLabel.config(text="Correo Electrónico:")

raiz.mainloop()