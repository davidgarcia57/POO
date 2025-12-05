from conexionBD import conexion, cursor

class Camiones:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        try:
            cursor.execute(
                "INSERT INTO camiones VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
                (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(id, marca):
        try:
            cursor.execute("UPDATE camiones SET marca=%s WHERE id=%s", (marca, id))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False