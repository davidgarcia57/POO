from tkinter import messagebox
from model import autos
from model import camiones
from model import camionetas

class Controladores:

    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo, message="¡Acción realizada con éxito!")
        else:
            messagebox.showerror(title=titulo, message="No fue posible realizar la acción, verifique datos.")

    @staticmethod
    def insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
        if marca and modelo:
            respuesta = autos.Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)
            Controladores.respuesta_sql("Insertar Auto", respuesta)
        else:
            messagebox.showwarning("Atención", "Campos obligatorios vacíos")

    @staticmethod
    def consultar_autos():
        return autos.Autos.consultar()

    @staticmethod
    def cambiar_auto(id, marca):
        if id and marca:
            respuesta = autos.Autos.actualizar(id, marca)
            Controladores.respuesta_sql("Actualizar Auto", respuesta)
        else:
            messagebox.showwarning("Atención", "Faltan datos")

    @staticmethod
    def borrar_auto(id):
        if id:
            respuesta = autos.Autos.eliminar(id)
            Controladores.respuesta_sql("Borrar Auto", respuesta)
        else:
            messagebox.showwarning("Atención", "Ingrese el ID")

    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if marca and modelo:
            respuesta = camionetas.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            Controladores.respuesta_sql("Insertar Camioneta", respuesta)
        else:
            messagebox.showwarning("Atención", "Campos obligatorios vacíos")

    @staticmethod
    def consultar_camionetas():
        return camionetas.Camionetas.consultar()

    @staticmethod
    def cambiar_camioneta(id, marca):
        if id and marca:
            respuesta = camionetas.Camionetas.actualizar(id, marca)
            Controladores.respuesta_sql("Actualizar Camioneta", respuesta)
        else:
            messagebox.showwarning("Atención", "Faltan datos")

    @staticmethod
    def borrar_camioneta(id):
        if id:
            respuesta = camionetas.Camionetas.eliminar(id)
            Controladores.respuesta_sql("Borrar Camioneta", respuesta)
        else:
            messagebox.showwarning("Atención", "Ingrese el ID")

    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, ejes, carga):
        if marca and modelo:
            respuesta = camiones.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, ejes, carga)
            Controladores.respuesta_sql("Insertar Camión", respuesta)
        else:
            messagebox.showwarning("Atención", "Campos obligatorios vacíos")

    @staticmethod
    def consultar_camiones():
        return camiones.Camiones.consultar()

    @staticmethod
    def cambiar_camion(id, marca):
        if id and marca:
            respuesta = camiones.Camiones.actualizar(id, marca)
            Controladores.respuesta_sql("Actualizar Camión", respuesta)
        else:
            messagebox.showwarning("Atención", "Faltan datos")

    @staticmethod
    def borrar_camion(id):
        if id:
            respuesta = camiones.Camiones.eliminar(id)
            Controladores.respuesta_sql("Borrar Camión", respuesta)
        else:
            messagebox.showwarning("Atención", "Ingrese el ID")