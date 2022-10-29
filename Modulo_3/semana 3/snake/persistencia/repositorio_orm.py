from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class RepositorioConexionORMSQLite:    

    def __init__(self) -> None:
        pass

    def conetarse(self):
        try:
            self.engine = create_engine("sqlite:///./somedb.db", echo=True, future=True)
            
        except Exception as e:
            print("Error al leer los datos de la tabla ORM", e)

    def cerrar_conexion(self):
        pass                    
