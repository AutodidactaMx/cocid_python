import mysql.connector
from persistencia.repositorio_conexion import RepositorioConexion
from dominio.objetos.persona import Persona


class RepositorioPersona (RepositorioConexion):

    def __init__(self) -> None:
        super().__init__()

    def insertar(self, persona: Persona) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO prowebco_cocid.tb_persona
            (curp, nombre, edad, correo, telefono)
            VALUES(%s, %s, %s, %s, %s);
            """
            registros = (persona.curp, persona.nombre,
                         persona.edad, persona.correo, persona.telefono)

            cursor.execute(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado
