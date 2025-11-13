from tkinter import messagebox

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

            messagebox.showinfo(icon="info", title=titulo, message=f"{numero1} {simbolo} {numero2} = {resultado}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió el siguiente error: {e}")