from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import funciones

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Coches System")
        self.ventana.geometry("700x600")
        self.ventana.resizable(False, False)
        self.menu_principal(self.ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=".::MENU PRINCIPAL::.", font=("Arial", 20, "bold"), justify="center")
        lbl_titulo.pack(pady=30)

        boton_autos = Button(ventana, text="1.- Autos", width=20, height=2, command=lambda: Vistas.menu_acciones(ventana, "Autos"))
        boton_autos.pack(pady=10)

        boton_camionetas = Button(ventana, text="2.- Camionetas", width=20, height=2, command=lambda: Vistas.menu_acciones(ventana, "Camionetas"))
        boton_camionetas.pack(pady=10)

        boton_camiones = Button(ventana, text="3.- Camiones", width=20, height=2, command=lambda: Vistas.menu_acciones(ventana, "Camiones"))
        boton_camiones.pack(pady=10)

        boton_salir = Button(ventana, text="4.- Salir", width=20, height=2, bg="#F44336", fg="white", command=ventana.quit)
        boton_salir.pack(pady=10)

    @staticmethod
    def menu_acciones(ventana, tipo):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f"Menú {tipo}", font=("Arial", 18, "bold"), justify="center")
        lbl_titulo.pack(pady=20)

        cmd_insertar = None
        cmd_consultar = None
        cmd_cambiar = None
        cmd_borrar = None

        if tipo == "Autos":
            cmd_insertar = lambda: Vistas.insertar_autos(ventana)
            cmd_consultar = lambda: Vistas.consultar_autos(ventana)
            cmd_cambiar = lambda: Vistas.cambiar_autos(ventana)
            cmd_borrar = lambda: Vistas.borrar_autos(ventana)
        elif tipo == "Camionetas":
            cmd_insertar = lambda: Vistas.insertar_camionetas(ventana)
            cmd_consultar = lambda: Vistas.consultar_camionetas(ventana)
            cmd_cambiar = lambda: Vistas.cambiar_camionetas(ventana)
            cmd_borrar = lambda: Vistas.borrar_camionetas(ventana)
        elif tipo == "Camiones":
            cmd_insertar = lambda: Vistas.insertar_camiones(ventana)
            cmd_consultar = lambda: Vistas.consultar_camiones(ventana)
            cmd_cambiar = lambda: Vistas.cambiar_camiones(ventana)
            cmd_borrar = lambda: Vistas.borrar_camiones(ventana)

        boton_insertar = Button(ventana, text="Insertar", width=20, command=cmd_insertar)
        boton_insertar.pack(pady=5)

        boton_consultar = Button(ventana, text="Consultar", width=20, command=cmd_consultar)
        boton_consultar.pack(pady=5)

        boton_actualizar = Button(ventana, text="Actualizar", width=20, command=cmd_cambiar)
        boton_actualizar.pack(pady=5)

        boton_borrar = Button(ventana, text="Borrar", width=20, command=cmd_borrar)
        boton_borrar.pack(pady=5)

        boton_volver = Button(ventana, text="Volver", width=20, command=lambda: Vistas.menu_principal(ventana))
        boton_volver.pack(pady=20)

    @staticmethod
    def insertar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Insertar Auto", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=2)

        lbl_color = Label(ventana, text="Color:")
        lbl_color.pack()
        entry_color = Entry(ventana, width=30)
        entry_color.pack(pady=2)

        lbl_modelo = Label(ventana, text="Modelo:")
        lbl_modelo.pack()
        entry_modelo = Entry(ventana, width=30)
        entry_modelo.pack(pady=2)

        lbl_velocidad = Label(ventana, text="Velocidad:")
        lbl_velocidad.pack()
        entry_velocidad = Entry(ventana, width=30)
        entry_velocidad.pack(pady=2)

        lbl_caballaje = Label(ventana, text="Caballaje:")
        lbl_caballaje.pack()
        entry_caballaje = Entry(ventana, width=30)
        entry_caballaje.pack(pady=2)

        lbl_plazas = Label(ventana, text="Plazas:")
        lbl_plazas.pack()
        entry_plazas = Entry(ventana, width=30)
        entry_plazas.pack(pady=2)

        boton_guardar = Button(ventana, text="Guardar", bg="#4CAF50", fg="white",
                               command=lambda: funciones.Controladores.insertar_auto(
                                   entry_marca.get(), entry_color.get(), entry_modelo.get(),
                                   entry_velocidad.get(), entry_caballaje.get(), entry_plazas.get()))
        boton_guardar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Autos"))
        boton_volver.pack(pady=5)

    @staticmethod
    def consultar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Consultar Autos", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas")
        tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=90, anchor="center")
        tree.pack(fill="both", expand=True, padx=10)

        registros = funciones.Controladores.consultar_autos()
        for fila in registros:
            tree.insert("", "end", values=fila)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Autos"))
        boton_volver.pack(pady=10)

    @staticmethod
    def cambiar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Cambiar Auto", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID del Auto a cambiar:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=2)

        lbl_color = Label(ventana, text="Color:")
        lbl_color.pack()
        entry_color = Entry(ventana, width=30)
        entry_color.pack(pady=2)

        lbl_modelo = Label(ventana, text="Modelo:")
        lbl_modelo.pack()
        entry_modelo = Entry(ventana, width=30)
        entry_modelo.pack(pady=2)

        lbl_velocidad = Label(ventana, text="Velocidad:")
        lbl_velocidad.pack()
        entry_velocidad = Entry(ventana, width=30)
        entry_velocidad.pack(pady=2)

        lbl_caballaje = Label(ventana, text="Caballaje:")
        lbl_caballaje.pack()
        entry_caballaje = Entry(ventana, width=30)
        entry_caballaje.pack(pady=2)

        lbl_plazas = Label(ventana, text="Plazas:")
        lbl_plazas.pack()
        entry_plazas = Entry(ventana, width=30)
        entry_plazas.pack(pady=2)

        boton_actualizar = Button(ventana, text="Actualizar", bg="#FFC107",
                                  command=lambda: funciones.Controladores.cambiar_auto(entry_id.get(), entry_marca.get(), entry_color.get(), entry_modelo.get(), entry_velocidad.get(), entry_caballaje.get(), entry_plazas.get()))
        boton_actualizar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Autos"))
        boton_volver.pack(pady=5)

    @staticmethod
    def borrar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Borrar Auto", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID del Auto a borrar:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        boton_borrar = Button(ventana, text="Borrar", bg="#F44336", fg="white",
                              command=lambda: funciones.Controladores.borrar_auto(entry_id.get()))
        boton_borrar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Autos"))
        boton_volver.pack(pady=5)

    @staticmethod
    def insertar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Insertar Camioneta", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=2)

        lbl_color = Label(ventana, text="Color:")
        lbl_color.pack()
        entry_color = Entry(ventana, width=30)
        entry_color.pack(pady=2)

        lbl_modelo = Label(ventana, text="Modelo:")
        lbl_modelo.pack()
        entry_modelo = Entry(ventana, width=30)
        entry_modelo.pack(pady=2)

        lbl_velocidad = Label(ventana, text="Velocidad:")
        lbl_velocidad.pack()
        entry_velocidad = Entry(ventana, width=30)
        entry_velocidad.pack(pady=2)

        lbl_caballaje = Label(ventana, text="Caballaje:")
        lbl_caballaje.pack()
        entry_caballaje = Entry(ventana, width=30)
        entry_caballaje.pack(pady=2)

        lbl_plazas = Label(ventana, text="Plazas:")
        lbl_plazas.pack()
        entry_plazas = Entry(ventana, width=30)
        entry_plazas.pack(pady=2)

        lbl_traccion = Label(ventana, text="Tracción:")
        lbl_traccion.pack()
        entry_traccion = Entry(ventana, width=30)
        entry_traccion.pack(pady=2)

        var_cerrada = BooleanVar()
        check_cerrada = Checkbutton(ventana, text="¿Es Cerrada?", variable=var_cerrada)
        check_cerrada.pack(pady=2)

        boton_guardar = Button(ventana, text="Guardar", bg="#4CAF50", fg="white",
                               command=lambda: funciones.Controladores.insertar_camioneta(
                                   entry_marca.get(), entry_color.get(), entry_modelo.get(),
                                   entry_velocidad.get(), entry_caballaje.get(), entry_plazas.get(),
                                   entry_traccion.get(), var_cerrada.get()))
        boton_guardar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camionetas"))
        boton_volver.pack(pady=5)

    @staticmethod
    def consultar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Consultar Camionetas", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Trac", "Cerr")
        tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=70, anchor="center")
        tree.pack(fill="both", expand=True, padx=10)

        registros = funciones.Controladores.consultar_camionetas()
        for fila in registros:
            tree.insert("", "end", values=fila)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camionetas"))
        boton_volver.pack(pady=10)

    @staticmethod
    def cambiar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Cambiar Camioneta", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la Camioneta:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Nueva Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=5)

        boton_actualizar = Button(ventana, text="Actualizar", bg="#FFC107",
                                  command=lambda: funciones.Controladores.cambiar_camioneta(entry_id.get(), entry_marca.get()))
        boton_actualizar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camionetas"))
        boton_volver.pack(pady=5)

    @staticmethod
    def borrar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Borrar Camioneta", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la Camioneta:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        boton_borrar = Button(ventana, text="Borrar", bg="#F44336", fg="white",
                              command=lambda: funciones.Controladores.borrar_camioneta(entry_id.get()))
        boton_borrar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camionetas"))
        boton_volver.pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Insertar Camión", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_marca = Label(ventana, text="Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=2)

        lbl_color = Label(ventana, text="Color:")
        lbl_color.pack()
        entry_color = Entry(ventana, width=30)
        entry_color.pack(pady=2)

        lbl_modelo = Label(ventana, text="Modelo:")
        lbl_modelo.pack()
        entry_modelo = Entry(ventana, width=30)
        entry_modelo.pack(pady=2)

        lbl_velocidad = Label(ventana, text="Velocidad:")
        lbl_velocidad.pack()
        entry_velocidad = Entry(ventana, width=30)
        entry_velocidad.pack(pady=2)

        lbl_caballaje = Label(ventana, text="Caballaje:")
        lbl_caballaje.pack()
        entry_caballaje = Entry(ventana, width=30)
        entry_caballaje.pack(pady=2)

        lbl_plazas = Label(ventana, text="Plazas:")
        lbl_plazas.pack()
        entry_plazas = Entry(ventana, width=30)
        entry_plazas.pack(pady=2)

        lbl_ejes = Label(ventana, text="Ejes:")
        lbl_ejes.pack()
        entry_ejes = Entry(ventana, width=30)
        entry_ejes.pack(pady=2)

        lbl_carga = Label(ventana, text="Carga:")
        lbl_carga.pack()
        entry_carga = Entry(ventana, width=30)
        entry_carga.pack(pady=2)

        boton_guardar = Button(ventana, text="Guardar", bg="#4CAF50", fg="white",
                               command=lambda: funciones.Controladores.insertar_camion(
                                   entry_marca.get(), entry_color.get(), entry_modelo.get(),
                                   entry_velocidad.get(), entry_caballaje.get(), entry_plazas.get(),
                                   entry_ejes.get(), entry_carga.get()))
        boton_guardar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camiones"))
        boton_volver.pack(pady=5)

    @staticmethod
    def consultar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Consultar Camiones", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Ejes", "Carga")
        tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=70, anchor="center")
        tree.pack(fill="both", expand=True, padx=10)

        registros = funciones.Controladores.consultar_camiones()
        for fila in registros:
            tree.insert("", "end", values=fila)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camiones"))
        boton_volver.pack(pady=10)

    @staticmethod
    def cambiar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Cambiar Camión", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID del Camión:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        lbl_marca = Label(ventana, text="Nueva Marca:")
        lbl_marca.pack()
        entry_marca = Entry(ventana, width=30)
        entry_marca.pack(pady=5)

        boton_actualizar = Button(ventana, text="Actualizar", bg="#FFC107",
                                  command=lambda: funciones.Controladores.cambiar_camion(entry_id.get(), entry_marca.get()))
        boton_actualizar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camiones"))
        boton_volver.pack(pady=5)

    @staticmethod
    def borrar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text="Borrar Camión", font=("Arial", 16))
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID del Camión:")
        lbl_id.pack()
        entry_id = Entry(ventana, width=30)
        entry_id.pack(pady=5)

        boton_borrar = Button(ventana, text="Borrar", bg="#F44336", fg="white",
                              command=lambda: funciones.Controladores.borrar_camion(entry_id.get()))
        boton_borrar.pack(pady=10)

        boton_volver = Button(ventana, text="Volver", command=lambda: Vistas.menu_acciones(ventana, "Camiones"))
        boton_volver.pack(pady=5)