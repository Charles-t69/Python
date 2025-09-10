from tkinter import *
raiz= Tk()
raiz.title("Titulo de prueba")
# raiz.resizable(0,0)
raiz.resizable(True,False)
raiz.iconbitmap("social.ico")
# raiz.geometry("600x400")
raiz.config(bg="cyan")
miFrame= Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="600",height="400")

miFrame.pack(side="right", anchor="n",fill="x")

'''miFrame.pack(side="right")
miFrame.pack(side="right", anchor="n")
miFrame.pack(fill="x")'''

miFrame.pack(fill="both", expand=True)

miFrame.config(bg="red", relief="groove", cursor="hand2")

''' miFrame.config(bg="red")
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")'''

raiz.config(bg="cyan", relief="groove", cursor="hand2")

'''raiz.config(bd=30)
raiz.config("groove")
raiz.config(cursor="hand2")'''

raiz.mainloop()
