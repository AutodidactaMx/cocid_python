from persistencia.conexion import RepositorioConexionSQLite
from modelo.ventas_servicio_model import VentasServicioModel


class VentasServicioPersistencia (RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()

    def insertarMany(self, ventas):
        try:
            super().conetarse()
            mySql_insert_query = f"""INSERT INTO ventas_servicio 
            (servicio, total, fecha_hora_venta) VALUES(?, ?, ?);                     
            """
            cursor = self.connection.cursor()
            values = []
            print("Generando datos")
            for row in ventas:
                values.append((row.servicio, row.total,
                               row.fecha_hora_venta))
            print("Guardando ...")
            cursor.executemany(mySql_insert_query, values)
            self.connection.commit()
            print("Finalizo")
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
            self.connection.rollback()

    def consultarTodo(self) -> list:
        ventas: list = []
        try:
            super().conetarse()
            sql_select_query = """
                SELECT servicio, total, fecha_hora_venta FROM ventas_servicio
                """
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentasServicioModel(
                    servicio=row[0], total=row[1], fecha_hora_venta=row[2])
                ventas.append(venta)
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
        return ventas