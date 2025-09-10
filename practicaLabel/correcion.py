from tkinter import *
from PIL import Image, ImageTk

raiz = Tk()
raiz.title("Título de prueba")
raiz.geometry("600x400")
raiz.resizable(True, False)

# Icono .ico (asegúrate de que sena2.ico exista y sea 32x32)
raiz.iconbitmap(r"C:\Users\Aprendiz\Documents\GitHub\Python\primer_interface\sena2.ico")

raiz.config(bg="cyan")

# Frame
miFrame = Frame(raiz, width=600, height=400, bg="red", relief="groove", cursor="hand2")
miFrame.pack(fill="both", expand=True)

# Label de texto
Label(miFrame, text="Esta es una práctica de Labels de Python",
      fg="blue", font=("Comic Sans MS", 14)).place(x=100, y=200)

# Imagen con Pillow
imagen = Image.open(r"C:\Users\Aprendiz\Documents\GitHub\Python\practicaLabel\1111.png")
miImagen = ImageTk.PhotoImage(imagen)
Label(miFrame, image=miImagen).place(x=125, y=75)

raiz.mainloop()
