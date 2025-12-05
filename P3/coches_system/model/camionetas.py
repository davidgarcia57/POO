from conexionBD import conexion, cursor

class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        cerrada_int = 1 if cerrada else 0
        try:
            cursor.execute(
                "INSERT INTO camionetas VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
                (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_int)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_int):
        try:
            cursor.execute("UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s", (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_int, id))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camionetas WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def buscar(id):
        try:
            cursor.execute("SELECT * FROM camionetas WHERE id=%s", (id,))
            return cursor.fetchone()
        except:
            return None