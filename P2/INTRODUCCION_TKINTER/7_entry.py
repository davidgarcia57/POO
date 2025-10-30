from tkinter import *

ventana = Tk()
ventana.title("Entry")
ventana.geometry("500x500")

def cambiar():
    nombre= entrada1.get()
    etiqueta2.config(text=f"Hola {nombre} bienvenido")

etiqute1=Label(ventana, text="Ingrese su nombre: ").pack()

entrada1=Entry(ventana)
entrada1.pack()

boton1=Button(ventana,text="Saludar",command= cambiar)
boton1.pack()

etiqueta2=Label(ventana, text="")
etiqueta2.pack()

ventana.mainloop()