import mysql.connector
from persistencia.repositorio_conexion import RepositorioConexion
from persistencia.respositorio_conexion_sql import RepositorioConexionSQLite
from dominio.objetos.persona import Persona


class RepositorioPersona (RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()
        
    def contruir_tabla(self):
        error = 0
        try:
            super().conetarse()
            self.cur = self.connection.cursor()
            sql = """            
                CREATE TABLE tb_persona (
                curp varchar(100) NOT NULL,
                nombre varchar(100) DEFAULT NULL,
                edad varchar(100) DEFAULT NULL,
                correo varchar(100) DEFAULT NULL,
                telefono varchar(100) DEFAULT NULL,
                PRIMARY KEY (curp)
                ) 
            """
            self.cur.execute(sql)
            self.connection.commit()
        except :
            error=1
        return error   

    def insertar(self, persona: Persona) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO tb_persona
            (curp, nombre, edad, correo, telefono)
            VALUES(?, ?, ?, ?, ?);
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

    def eliminar(self, curp) -> int:
        afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_eliminar_query = """DELETE FROM tb_persona
            WHERE curp=?;
            """            
            eliminar = (curp,)
            cursor.execute(mySql_eliminar_query,eliminar)
            self.connection.commit()
            afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return afectado

    
    def consultar(self) -> list:
        personas: list = []
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select * from tb_persona"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
                persona = Persona().asignar(curp=row[0], nombre=row[1],
                                  edad=row[2], correo=row[3], telefono=row[4])
                personas.append(persona)

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return personas
