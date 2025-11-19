from tkinter import messagebox
from model import operaciones

#Controlador

class Controladores:

    @staticmethod
    def operaciones(titulo, numero1, numero2, simbolo):
        try:
            if simbolo == "+":
                resultado = numero1 + numero2
            elif simbolo == "-":
                resultado = numero1 - numero2
            elif simbolo == "x":
                resultado = numero1 * numero2
            elif simbolo == "/":
                if numero2 == 0:
                    messagebox.showerror("Error", "No se puede dividir por cero")
                    return
                resultado = numero1 / numero2
            else:
                messagebox.showerror("Error", f"Operación desconocida: {simbolo}")
                return
            result=messagebox.askquestion( message=f"{numero1} {simbolo} {numero2} = {resultado}\n ¿Quires guardar la operación en la BD?",icon="question")
            if result =="yes":
                operaciones.Operaciones.insertar(numero1, numero2, simbolo, resultado)
            #messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {simbolo} {numero2} = {resultado}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió el siguiente error: {e}")