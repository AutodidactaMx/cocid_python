from persistencia.conexion import RepositorioConexionSQLite
from modelos.modelo_venta_consulta import VentaDepartamento
from modelos.modelo_cbx import ModeloCombo


class VentasPersistencia (RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()

    def insertarMany(self, ventas):
        try:
            super().conetarse()
            mySql_insert_query = f"""INSERT INTO ventas_semanales
            (tienda, departamento, fecha, ventas, es_vacaciones)            
            VALUES(?, ?, ?, ?, ?);
            """
            cursor = self.connection.cursor()
            values = []
            print("Generando datos")
            for row in ventas:
                values.append((row.tienda, row.departamento,
                               row.fecha, row.ventasSemanales, row.esVacaciones))
            print("Guardando ...")
            cursor.executemany(mySql_insert_query, values)
            self.connection.commit()
            print("Finalizo")
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
            self.connection.rollback()

    def ventasPorDepartamento(self, opcion = None) -> list:
        ventas: list = []
        try:
            super().conetarse()
            sql_select_query = """
                select tienda , departamento , sum(ventas) as ventas from ventas_semanales
                group by tienda , departamento
                """

            if(opcion != 0):
                sql_select_query = f"""
                select tienda , departamento , sum(ventas) as ventas from ventas_semanales
                where departamento = {opcion}
                group by tienda , departamento
                """
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentaDepartamento(
                    tienda=row[0], departamento=row[1], ventas=row[2])
                ventas.append(venta)
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
        return ventas

    def ObtenerDepartamentos(self) -> list:
        ventas: list = []
        try:
            super().conetarse()
            sql_select_query = """
            select departamento from ventas_semanales
            group by departamento
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                ventas.append(ModeloCombo(id=row[0],descripcion=f"{row[0]}"))
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
        return ventas
