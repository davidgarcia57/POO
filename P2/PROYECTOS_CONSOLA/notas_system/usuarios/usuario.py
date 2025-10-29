
from conexionBD import *
import hashlib
import datetime

class Usuarios:
    
    @staticmethod
    def registrar(nombre,apellidos,email,contrasena):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
            "insert into usuarios values(null,%s,%s,%s,%s,%s)",
            (nombre,apellidos,email,contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            cursor.execute(
            "select * from usuarios where email=%s and password=%s",
            (email,contrasena))
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return None      
        except:
            return None         