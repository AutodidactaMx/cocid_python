import sqlite3

class RepositorioConexionSQLite:
    connection: any

    def __init__(self) -> None:
        pass

    def conetarse(self):
        try:
            self.connection = sqlite3.connect("BaseDatosLocal.db")
            
        except Exception as e:
            print("Error al leer los datos de la tabla MySQL", e)

    def cerrar_conexion(self):
        pass                    
