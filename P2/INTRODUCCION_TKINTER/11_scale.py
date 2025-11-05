from tkinter import * 

ventana = Tk()
ventana.title("scale")
ventana.geometry("500x500")

def mostrarEstado():
    resultado.config(text="El Valo es: ")

barra = Scale(ventana, orient="vertical")
barra.pack()

boton=Button(ventana, text="Mostrar Valor", command=mostrarEstado)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()