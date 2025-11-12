from tkinter import messagebox

#Controlador
def suma(numero1,numero2):
    suma=numero1+numero2
    messagebox.showinfo(icon="info", title="Suma", message=f"{numero1} + {numero2} = {suma}")

def resta(numero1,numero2):
     resta=numero1-numero2
     messagebox.showinfo(icon="info", title="Resta", message=f"{numero1} + {numero2} = {resta}")

def multiplicacion(numero1,numero2):
     multiplicacion=numero1*numero2
     messagebox.showinfo(icon="info", title="Multiplicación", message=f"{numero1} + {numero2} = {multiplicacion}")

def division(numero1,numero2):
    division=numero1/numero2
    messagebox.showinfo(icon="info", title="División", message=f"{numero1} + {numero2} = {division}")