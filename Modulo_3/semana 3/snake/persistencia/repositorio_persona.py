import mysql.connector
from persistencia.repositorio_orm import RepositorioConexionORMSQLite
from persistencia.modelos import Persona
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import persistencia.modelos as mod


class RepositorioPersona (RepositorioConexionORMSQLite):

    def __init__(self) -> None:
        super().__init__()
        
    def contruir_tabla(self):
        error = 0
        try:
            super().conetarse()                        
            mod.Base.metadata.create_all(self.engine)
        except Exception as e:
            print(e)
            error=1
        return error   

    def insertar(self, persona: Persona) -> int:
        registros_afectado = 1
        try:
            super().conetarse()
            with Session(self.engine) as session:            
                session.add(persona)
                session.commit() 

        except Exception as error:
            registros_afectado = 0
            print(f"Fallo la insercion {error}")                    

        return registros_afectado

    def eliminar(self, curp) -> int:
        afectado = 1
        try:
            super().conetarse()
            with Session(self.engine) as session:        
                x = session.query(Persona).get(curp)
                session.delete(x)
                session.commit()                
        except Exception as error:
            afectado = 0
            print(f"Fallo la insercion {error}")        

        return afectado

    
    def consultar(self) -> list:
        personas: list = []
        try:
            super().conetarse()
            with Session(self.engine) as session:        
                result = session.query(Persona)
                
            for persona in result:                
                personas.append(persona)

        except Exception as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return personas
