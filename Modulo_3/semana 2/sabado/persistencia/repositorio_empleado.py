import mysql.connector
from persistencia.repositorio_conexion import RepositorioConexion
from dominio.objetos.empleado import Empleado


class RepositorioEmpleado (RepositorioConexion):

    def __init__(self) -> None:
        super().__init__()

    def insertar(self, empleado: Empleado) -> int:
        registros_afectado = 0
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            mySql_insert_query = """INSERT INTO prowebco_cocid.tb_empleado
            (curp, nombre, edad, correo, telefono, puesto, sueldo_dario, bono_mensual)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);

            """
            registros = (empleado.curp, empleado.nombre,
                         empleado.edad, empleado.correo, empleado.telefono, empleado.puesto, empleado.sueldo_diario, empleado.bono_mensual)

            cursor.execute(mySql_insert_query, registros)
            self.connection.commit()
            registros_afectado = cursor.rowcount
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

        return registros_afectado

    def consultar(self) -> list:
        empelado: list = []
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select * from prowebco_cocid.tb_empleado"
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                persona = Empleado().asignar(curp=row["curp"], nombre=row["nombre"],
                                            edad=row["edad"], correo=row["correo"], 
                                            telefono=row["telefono"],puesto=row["puesto"],
                                            sueldo_diario=row["sueldo_dario"],
                                            bono_mensual=row["bono_mensual"])
                empelado.append(persona)

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return empelado
