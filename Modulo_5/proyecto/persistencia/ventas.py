from persistencia.conexion import RepositorioConexionSQLite
from modelo.ventas_model import VentasModel


class VentasPersistencia (RepositorioConexionSQLite):

    def __init__(self) -> None:
        super().__init__()

    def insertarMany(self, ventas):
        try:
            super().conetarse()
            mySql_insert_query = f"""INSERT INTO ventas (id, descuento, total, propina, modo_pago, fecha_hora_venta)
            VALUES(?, ?, ?, ?, ?, ?);                       
            """
            cursor = self.connection.cursor()
            values = []
            print("Generando datos")
            for row in ventas:
                values.append((row.id, row.descuento,
                               row.total, row.propina, row.modo_pago, row.fecha_hora_venta))
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
                SELECT id, descuento, total, propina, modo_pago, fecha_hora_venta FROM ventas
                """
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentasModel(
                    id=row[0], descuento=row[1], total=row[2], propina=row[3], 
                    modo_pago=row[4], fecha_hora_venta=row[5])
                ventas.append(venta)
            cursor.close()
        except Exception as error:
            print(f"Fallo la insercion {error}")
        return ventas