from controller import funciones
from tkinter import *

#Interfaz o View

class Vistas:
    def __init__(self,ventana):
        ventana.title("...Calculadora Básica...")
        ventana.geometry("1024x768")
        ventana.resizable(False,False)
        self.interfaz(ventana)
        

    def menuPrincipal(self,ventana):
        menuBar= Menu(ventana)
        ventana.config(menu=menuBar)
        archivoMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciónes", menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: "")
        archivoMenu.add_command(label="Consultar",command=lambda:"")
        archivoMenu.add_command(label="Cambiar",command=lambda:"")
        archivoMenu.add_command(label="Borrar",command=lambda: "")
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=ventana.quit)
    
    def eliminar(self,ventana):
        label_titulo=Label(ventana, text=".::Borrar una Operación::.")
        label_titulo.pack()
        label_titulo.config(
        font=("Arial", 18)
        )

        label_id=Label(ventana, text=".::Borrar una Operación::.")
        label_id.pack()
        label_id.config(
        font=("Arial", 12)
        )

        entry_id=Entry(ventana)
        entry_id.pack()

        boton_eliminar=Button(ventana, text="Eliminar")
        boton_eliminar.pack()

        boton_volver=Button(ventana, text="Volver")
        boton_volver.pack()

    def interfaz(self,ventana):

        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.pack(pady=5)

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(pady=5)

        btn_suma=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()
        
        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack(pady=10)
