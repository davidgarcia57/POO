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
    def cambiar_auto(id, marca, color, modelo, velocidad, caballaje, plazas):
        if not id:
            messagebox.showwarning("Atención", "El ID es obligatorio")
            return
        auto_actual = autos.Autos.buscar(id)
        
        if auto_actual:
            nueva_marca = marca if marca else auto_actual[1]
            nuevo_color = color if color else auto_actual[2]
            nuevo_modelo = modelo if modelo else auto_actual[3]
            nueva_velocidad = velocidad if velocidad else auto_actual[4]
            nuevo_caballaje = caballaje if caballaje else auto_actual[5]
            nuevas_plazas = plazas if plazas else auto_actual[6]

            respuesta = autos.Autos.actualizar(id, nueva_marca, nuevo_color, nuevo_modelo, nueva_velocidad, nuevo_caballaje, nuevas_plazas)
            Controladores.respuesta_sql("Actualizar Auto", respuesta)
        else:
            messagebox.showerror("Error", f"No se encontró un auto con ID {id}")

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
    def cambiar_camioneta(id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if not id:
            messagebox.showwarning("Atención", "El ID es obligatorio")
            return
        camioneta_actual = camionetas.Camionetas.buscar(id)

        if camioneta_actual:
            nueva_marca = marca if marca else camioneta_actual[1]
            nuevo_color = color if color else camioneta_actual[2]
            nuevo_modelo = modelo if modelo else camioneta_actual[3]
            nueva_velocidad = velocidad if velocidad else camioneta_actual[4]
            nuevo_caballaje = caballaje if caballaje else camioneta_actual[5]
            nuevas_plazas = plazas if plazas else camioneta_actual[6]
            nueva_traccion = traccion if traccion else camioneta_actual[7]

            if cerrada is not None and cerrada != "":
                cerrada_str = str(cerrada).strip().lower()
                nueva_cerrada = 1 if cerrada_str in ("1", "true", "si", "s", "yes", "y") else 0
            else:
                nueva_cerrada = camioneta_actual[8]

            respuesta = camionetas.Camionetas.actualizar(id, nueva_marca, nuevo_color, nuevo_modelo, nueva_velocidad, nuevo_caballaje, nuevas_plazas, nueva_traccion, nueva_cerrada)
            Controladores.respuesta_sql("Actualizar Camioneta", respuesta)
        else:
            messagebox.showerror("Error", f"No se encontró una camioneta con ID {id}")

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
    def cambiar_camion(id, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        if not id:
            messagebox.showwarning("Atención", "El ID es obligatorio")
            return
        camion_actual = camiones.Camiones.buscar(id)

        if camion_actual:
            nueva_marca = marca if marca else camion_actual[1]
            nuevo_color = color if color else camion_actual[2]
            nuevo_modelo = modelo if modelo else camion_actual[3]
            nueva_velocidad = velocidad if velocidad else camion_actual[4]
            nuevo_caballaje = caballaje if caballaje else camion_actual[5]
            nuevas_plazas = plazas if plazas else camion_actual[6]
            nuevo_eje = eje if eje else camion_actual[7]
            nueva_capacidad = capacidadcarga if capacidadcarga else camion_actual[8]

            respuesta = camiones.Camiones.actualizar(id, nueva_marca, nuevo_color, nuevo_modelo, nueva_velocidad, nuevo_caballaje, nuevas_plazas, nuevo_eje, nueva_capacidad)
            Controladores.respuesta_sql("Actualizar Camión", respuesta)
        else:
            messagebox.showerror("Error", f"No se encontró un camión con ID {id}")