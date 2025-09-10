from tkinter import *

# 1. Crear la raíz del proyecto
raiz = Tk()

# 2. Colocar título a la ventana
raiz.title("Titulo de prueba")

# 3. Fijar tamaño de la ventana
raiz.geometry("600x400")

# 4. Redimensionar ventana (ejemplo: solo ancho)
raiz.resizable(True, False)   # True=ancho, False=alto

# 5. Agregar ícono a la ventana
raiz.iconbitmap("sena.ico")

# 6. Cambiar color de fondo de la ventana
raiz.config(bg="cyan")

# 7. Crear un frame dentro de la ventana
miFrame = Frame(raiz)

# 8. Empaquetar el frame (verás la ventana aparecer)
miFrame.pack()

# 9. Aplicar color al frame
miFrame.config(bg="red")

# 10. Redimensionar el frame
miFrame.config(width=600, height=400)

# 11. Fijar posición del frame (ejemplo: derecha arriba)
# miFrame.pack(side="right", anchor="n")

# 12. Ajustar el frame horizontalmente
# miFrame.pack(fill="x")

# 13. Ajustar el frame verticalmente
# miFrame.pack(fill="y")

# 14. Ajustar frame a toda la ventana
miFrame.pack(fill="both", expand=True)

# 15. Agregar borde y estilo al frame
miFrame.config(relief="sunken")

# 16. Cambiar cursor al pasar por el frame
miFrame.config(cursor="pirate")

# 17. Aplicar los mismos cambios al raíz (sin relief porque no aplica)
raiz.config(cursor="hand2")

# 18. El método mainloop SIEMPRE debe estar al final
raiz.mainloop()
