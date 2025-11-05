from tkinter import * 

ventana = Tk()
ventana.title("checkButton")
ventana.geometry("500x500")

def mostrarEstado():
    resultado.config(text=f"Opción Seleccionada: {opcion.get()}")

opcion = StringVar()
radioBoton1 = Radiobutton(ventana, text="Opción 1", variable=opcion, value="Opcion1")
radioBoton1.pack()

radioBoton2 = Radiobutton(ventana, text="Opción 2", variable=opcion, value="Opcion2")
radioBoton2.pack()

radioBoton3 = Radiobutton(ventana, text="Opción 3", variable=opcion, value="Opcion3")
radioBoton3.pack()

boton=Button(ventana, text="Mostrar Opción", command=mostrarEstado)
boton.pack()

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()