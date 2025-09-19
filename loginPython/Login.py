from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import time
import conexion

class Login(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        
        self.user_marca = "Ingrese a su correo"
        self.contra_marca = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.datos =conexion.Registro_datos()
        self.widgets()

    def entry_out(self, event, event_text):
        if event ['fg'] == 'black' and len(event.get()) ==0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.isert(0, event_text)

        if self.entry2.get() != 'Ingrese su contrasena':
            self.entry2['show'] == ""

        if self.entry2.get() != 'Ingrese su Correo':
            self.entry2['show'] == ""

    def entry_in(self, event):
        if event ['fg'] == 'grey' and len(event.get()) ==0:
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su contrasena':
            self.entry2['show'] == "*"

        if self.entry2.get() != 'Ingrese su contrasena':
            self.entry2['show'] == ""

    def salir(selt):
        selft.master.destroy()
        selft.master.quit()

    def acceder_ventana_dos(self):
        for i in range(101):
            self.barra['value'] +1
            self.master.update()
            time.sleep(0.02)

            self.master.withdraw()
            self.ventana_dos = Toplevel()
            self.ventana_dos.title('Segunda Ventana')
            self.ventana_dos.geometry('500x500+400+80')
            self.ventana_dos.protocol("WM_DELETE_WINDOW", self.salir)
            self.ventana_dos.config(bg='white')
            self.ventana_dos.state('zoomed')

            Label(self.ventana_dos, text='VENTANA DOS', font='ARIAL 40', bg='white').pack(expand=True)
            Button(self.ventana_dos, text='SALIR', font='ARIAL 10', bg='red').pack()

        def verification_user(self):
            self.indica1['text'] = ''
            self.indica1['text'] = ''
            users_entry = self.entry1.get()
            password_entry = self.entry2.get()

            dato1 = self.datos.busca_users(users_entry)
            dato2 = self.datos.busca_password(password_entry)
            
            self.fila1 = dato1
            self.filal2 = dato2

            if self.fila1 == self.fila2:
                if dato1 == [] and dato2 == []:
                    self.indica2['text'] = 'Contrasena Incorrecta'
                    self.indica1['text'] = 'Usuario Incorrecto'
                else:

                    if dato1 ==[]:
                        self.indica1['text'] = 'Usuario Incorrecto'
                    else:
                        dato1 = dato1[0][1]

                    if dato2 ==[]:
                        self.indica2['text'] = 'Contrasena Incorrecta'
                    else:
                        dato1 = dato1[0][2]

                    if dato1 !=[] and dato2 != []:
                        self.acceder_ventana_dos()

            else:
                self.indica2['text'] = 'Contrasena Incorrecta'
                self.indica1['text'] = 'Usuario Incorrecto'
                