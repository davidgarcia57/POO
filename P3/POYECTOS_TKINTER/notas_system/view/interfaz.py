from tkinter import *

class Vistas():
    def __init__(self,ventana):
        ventana.title("Gestión de Notas")
        ventana.geometry("500x400")
        ventana.resizable(False,False)
        self.menuPrincipal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menuPrincipal(self,ventana):
        self.borrarPantalla(ventana)
        label_titulo=Label(ventana, text=".::Menu principal::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        boton_registro=Button(ventana, text="1.-Registro",command=lambda: self.resgistroSistema(ventana))
        boton_registro.pack(pady=5)
        boton_registro.config()

        boton_login=Button(ventana, text="2.-Login", command=lambda: self.login(ventana))
        boton_login.pack(pady=5)
        boton_login.config()

        boton_salir=Button(ventana, text="3.-Salir")
        boton_salir.pack(pady=5)
        boton_salir.config()

    def login(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Inicio de Sesión::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_nombre=Label(ventana, text="¿Cual es tu nombre?:")
        lbl_nombre.pack(pady=5)
        lbl_nombre.config()
        entry_nombre=Entry(ventana, width=30)
        entry_nombre.pack(pady=5)

        lbl_apellidos=Label(ventana, text="¿Cuales son tus apellidos?:")
        lbl_apellidos.pack(pady=5)
        lbl_apellidos.config()
        entry_apellidos=Entry(ventana, width=30)
        entry_apellidos.pack(pady=5)

        lbl_email=Label(ventana, text="Ingresa tu email:")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30)
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30)
        entry_contrasena.pack(pady=5)

        boton_registrar=Button(ventana, text="Registrar")
        boton_registrar.pack(pady=5)
        boton_registrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menuPrincipal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()

    def resgistroSistema(self,ventana):
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=".::Registro en el Sistema::.")
        lbl_titulo.pack(pady=5)
        lbl_titulo.config()
        
        lbl_email=Label(ventana, text="Ingresa tu email:")
        lbl_email.pack(pady=5)
        lbl_email.config()
        entry_email=Entry(ventana, width=30)
        entry_email.pack(pady=5)

        lbl_contrasena=Label(ventana, text="Ingresa tu Contraseña:")
        lbl_contrasena.pack(pady=5)
        lbl_contrasena.config()
        entry_contrasena=Entry(ventana, width=30)
        entry_contrasena.pack(pady=5)

        boton_entrar=Button(ventana, text="Entrar")
        boton_entrar.pack(pady=5)
        boton_entrar.config()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.menuPrincipal(ventana))
        boton_volver.pack(pady=5)
        boton_volver.config()