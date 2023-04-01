import sqlite3

class RepositorioConexionSQLite:    

    def __init__(self) -> None:
        self.connection = None

    def conetarse(self):
        try:
            self.connection = sqlite3.connect("./bd/BaseDatosLocal3.db")
            
        except Exception as e:
            print("Error al leer los datos de la tabla MySQL", e)

    def cerrar_conexion(self):
        pass                    
