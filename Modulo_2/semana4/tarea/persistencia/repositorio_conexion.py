import mysql.connector


class RepositorioConexion:
    connection: any

    def __init__(self) -> None:
        pass

    def conetarse(self):
        try:
            self.connection = mysql.connector.connect(host='proweb-corp.com',
                                                 database='prowebco_cocid',
                                                 user='prowebco_alumnos_cocid',
                                                 password='qpF5n,QDotkU')
        except mysql.connector.Error as e:
            print("Error al leer los datos de la tabla MySQL", e)

    def cerrar_conexion(self):
        if self.connection.is_connected():
            self.connection.close()                        
