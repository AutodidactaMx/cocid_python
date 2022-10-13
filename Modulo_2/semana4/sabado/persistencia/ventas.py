import mysql.connector
from persistencia.conexion_bd import ConexionBD
from modelos.modelo_venta_consulta import VentaDepartamento, VentaTienda, VentaAnio


class VentasPersistencia (ConexionBD):

    def __init__(self) -> None:
        super().__init__()

    def insertarMany(self, ventas):
        try:
            super().conetarse()
            cursor = self.connection.cursor()
            mySql_insert_query = f"""INSERT INTO ventas_semanales
            (tienda, departamento, fecha, ventas, es_vacaciones)            
            VALUES(%s, %s, %s, %s, %s);
            """
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
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        except:
            self.connection.rollback()
        finally:
            self.cerrar_conexion()

    def ventasPorDepartamento(self) -> list:
        ventas: list = []
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = """
            select tienda , departamento , sum(ventas) as ventas from prowebco_cocid.ventas_semanales
            group by tienda , departamento
            """
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentaDepartamento(
                    row["tienda"], row["departamento"], row["ventas"])
                ventas.append(venta)

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return ventas

    def ventasPorTienda(self) -> list:
        ventas: list = []
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = """select tienda , sum(ventas) ventas from prowebco_cocid.ventas_semanales group by tienda 
            """
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentaTienda(row["tienda"], row["ventas"])
                ventas.append(venta)

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return ventas

    
    def ventasPorAnio(self) -> list:
        ventas: list = []
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = """
            SELECT YEAR (fecha) anio, sum(ventas) ventas
                FROM prowebco_cocid.ventas_semanales 
                group by YEAR (fecha) 
                order by YEAR (fecha) desc
            """
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
                venta = VentaAnio(row["anio"], row["ventas"])
                ventas.append(venta)

        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
        return ventas
