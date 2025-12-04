# from controller import funciones  <-- Descomenta esto cuando conectes el controlador
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Vistas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Coches system")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.menu_principal()
        self.lbl_bienvenida = Label(self.ventana, text="Bienvenido al Sistema\nSeleccione una opción del Menú", font=("Arial", 20))
        self.lbl_bienvenida.pack(expand=True)

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_principal(self):
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)
        menuArchivo = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Sistema", menu=menuArchivo)
        menuArchivo.add_command(label="Salir", command=self.ventana.quit)
        menuAutos = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Autos", menu=menuAutos)
        menuAutos.add_command(label="Insertar Auto", command=self.insertar_autos)
        menuAutos.add_command(label="Consultar Autos", command=self.consultar_autos)
        menuAutos.add_command(label="Cambiar Auto", command=self.cambiar_autos)
        menuAutos.add_command(label="Borrar Auto", command=self.borrar_autos)
        menuCamiones = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Camiones", menu=menuCamiones)
        menuCamiones.add_command(label="Insertar Camión", command=self.insertar_camiones)
        menuCamiones.add_command(label="Consultar Camiones", command=self.consultar_camiones)
        menuCamiones.add_command(label="Cambiar Camión", command=self.cambiar_camiones)
        menuCamiones.add_command(label="Borrar Camión", command=self.borrar_camiones)
        menuCamionetas = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Camionetas", menu=menuCamionetas)
        menuCamionetas.add_command(label="Insertar Camioneta", command=self.insertar_camionetas)
        menuCamionetas.add_command(label="Consultar Camionetas", command=self.consultar_camionetas)
        menuCamionetas.add_command(label="Cambiar Camioneta", command=self.cambiar_camionetas)
        menuCamionetas.add_command(label="Borrar Camioneta", command=self.borrar_camionetas)

    def menu_acciones(self, tipo):
        """
        Pantalla intermedia con botones grandes para elegir qué hacer 
        con el tipo de vehículo seleccionado (Insertar, Consultar, etc.)
        """
        self.borrarPantalla()
        self.menu_principal()
        Label(self.ventana, text=f"Menú de Acciones: {tipo.upper()}", font=("Arial", 18, "bold")).pack(pady=20)
        cmd_insertar = None
        cmd_consultar = None
        cmd_cambiar = None
        cmd_borrar = None
        if tipo == "Autos":
            cmd_insertar = self.insertar_autos
            cmd_consultar = self.consultar_autos
            cmd_cambiar = self.cambiar_autos
            cmd_borrar = self.borrar_autos
        elif tipo == "Camiones":
            cmd_insertar = self.insertar_camiones
            cmd_consultar = self.consultar_camiones
            cmd_cambiar = self.cambiar_camiones
            cmd_borrar = self.borrar_camiones
        elif tipo == "Camionetas":
            cmd_insertar = self.insertar_camionetas
            cmd_consultar = self.consultar_camionetas
            cmd_cambiar = self.cambiar_camionetas
            cmd_borrar = self.borrar_camionetas
        btn_frame = Frame(self.ventana)
        btn_frame.pack(pady=20)
        Button(btn_frame, text=f"Insertar {tipo}", width=20, height=2, command=cmd_insertar).grid(row=0, column=0, padx=10, pady=10)
        Button(btn_frame, text=f"Consultar {tipo}", width=20, height=2, command=cmd_consultar).grid(row=0, column=1, padx=10, pady=10)
        Button(btn_frame, text=f"Cambiar {tipo}", width=20, height=2, command=cmd_cambiar).grid(row=1, column=0, padx=10, pady=10)
        Button(btn_frame, text=f"Borrar {tipo}", width=20, height=2, command=cmd_borrar).grid(row=1, column=1, padx=10, pady=10)

    def insertar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR AUTO", font=("Arial", 16)).pack(pady=10)
        v_marca = StringVar()
        v_color = StringVar()
        v_modelo = StringVar()
        v_velocidad = IntVar()
        v_caballaje = IntVar()
        v_plazas = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "Marca:", v_marca)
        self._crear_entry(frm, "Color:", v_color)
        self._crear_entry(frm, "Modelo:", v_modelo)
        self._crear_entry(frm, "Velocidad:", v_velocidad)
        self._crear_entry(frm, "Caballaje:", v_caballaje)
        self._crear_entry(frm, "Plazas:", v_plazas)
        Button(self.ventana, text="Guardar Auto", bg="#4CAF50", fg="white",
               command=lambda: funciones.Controladores.insertar_auto(v_marca.get(), v_color.get(), v_modelo.get(), v_velocidad.get(), v_caballaje.get(), v_plazas.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def consultar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="CONSULTA DE AUTOS", font=("Arial", 16)).pack(pady=10)
        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas")
        tree = ttk.Treeview(self.ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.pack(fill="both", expand=True, padx=20, pady=10)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack(pady=10)

    def cambiar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR (ACTUALIZAR) AUTO", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        v_marca = StringVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID del Auto a cambiar:", v_id)
        self._crear_entry(frm, "Nueva Marca:", v_marca)
        Button(self.ventana, text="Actualizar", bg="#FFC107", 
               command=lambda: funciones.Controladores.cambiar_auto(v_id.get(), v_marca.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def borrar_autos(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR AUTO", font=("Arial", 16)).pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID del Auto a borrar:", v_id)
        Button(self.ventana, text="Eliminar Definitivamente", bg="#F44336", fg="white",
               command=lambda: funciones.Controladores.borrar_auto(v_id.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Autos")).pack()

    def insertar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR CAMIONETA", font=("Arial", 16)).pack(pady=10)
        v_vars = [StringVar() for _ in range(3)] + [IntVar() for _ in range(3)] + [StringVar(), BooleanVar()]
        (v_marca, v_color, v_modelo, v_vel, v_cab, v_pla, v_trac, v_cerrada) = v_vars
        frm = Frame(self.ventana)
        frm.pack()
        campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción"]
        for i, campo in enumerate(campos):
            Label(frm, text=campo+":").grid(row=i, column=0, sticky="e", pady=5)
            Entry(frm, textvariable=v_vars[i]).grid(row=i, column=1, pady=5)
        Checkbutton(frm, text="¿Es Cerrada?", variable=v_cerrada).grid(row=7, column=1, sticky="w")
        Button(self.ventana, text="Guardar Camioneta", bg="#4CAF50", fg="white",
               command=lambda: funciones.Controladores.insertar_camioneta(v_marca.get(), v_color.get(), v_modelo.get(), v_vel.get(), v_cab.get(), v_pla.get(), v_trac.get(), v_cerrada.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def consultar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="CONSULTA CAMIONETAS").pack(pady=10)
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Trac", "Cerrada")
        tree = ttk.Treeview(self.ventana, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=80)
        tree.pack(fill="both", expand=True)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack(pady=10)

    def cambiar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR CAMIONETA").pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID:", v_id)
        Button(self.ventana, text="Actualizar", bg="#FFC107", command=lambda: funciones.Controladores.cambiar_camioneta(v_id.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def borrar_camionetas(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR CAMIONETA").pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID:", v_id)
        Button(self.ventana, text="Borrar", bg="#F44336", fg="white", command=lambda: funciones.Controladores.borrar_camioneta(v_id.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camionetas")).pack()

    def insertar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="INSERTAR CAMIÓN", font=("Arial", 16)).pack(pady=10)
        v_vars = [StringVar(), StringVar(), StringVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        labels = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Cap. Carga"]
        frm = Frame(self.ventana)
        frm.pack()
        for i, txt in enumerate(labels):
            Label(frm, text=txt+":").grid(row=i, column=0, sticky="e", pady=5)
            Entry(frm, textvariable=v_vars[i]).grid(row=i, column=1, pady=5)
        Button(self.ventana, text="Guardar Camión", bg="#4CAF50", fg="white",
               command=lambda: funciones.Controladores.insertar_camion(*[v.get() for v in v_vars])).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def consultar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="CONSULTA CAMIONES").pack(pady=10)
        cols = ("ID", "Marca", "Color", "Modelo", "Vel", "Cab", "Pla", "Ejes", "Carga")
        tree = ttk.Treeview(self.ventana, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=80)
        tree.pack(fill="both", expand=True)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack(pady=10)

    def cambiar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="CAMBIAR CAMIÓN").pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID:", v_id)
        Button(self.ventana, text="Actualizar", bg="#FFC107", command=lambda: funciones.Controladores.cambiar_camion(v_id.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def borrar_camiones(self):
        self.borrarPantalla()
        Label(self.ventana, text="BORRAR CAMIÓN").pack(pady=10)
        v_id = IntVar()
        frm = Frame(self.ventana)
        frm.pack()
        self._crear_entry(frm, "ID:", v_id)
        Button(self.ventana, text="Borrar", bg="#F44336", fg="white", command=lambda: funciones.Controladores.borrar_camion(v_id.get())).pack(pady=20)
        Button(self.ventana, text="Volver", command=lambda: self.menu_acciones("Camiones")).pack()

    def _crear_entry(self, parent, text, variable):
        frame = Frame(parent)
        frame.pack(pady=2, fill="x")
        Label(frame, text=text, width=20, anchor="e").pack(side="left")
        Entry(frame, textvariable=variable).pack(side="left", expand=True, fill="x")