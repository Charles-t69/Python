from tkinter import *
root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miLabel=Label(miFrame, text="Esta es una práctica de Labels de Python", fg="blue", font=("comic Sans Ms", 14)).place(x=100, y=200)
miImagen= PhotoImage(file="veh.png")
Label(miFrame, image=miImagen).place(x=125, y=75)
root.mainloop()