import mysql.connector
from mysql.connector import Error
from const.conf import HOST,DATABASE,USER,PASSWORD

class ConexionBD :     
    connection: any

    def __init__(self) -> None:
        pass

    def conetarse(self):
        try:
            self.connection = mysql.connector.connect(host=HOST,
                                                 database=DATABASE,
                                                 user=USER,
                                                 password=PASSWORD)
        except mysql.connector.Error as e:
            print("Error al leer los datos de la tabla MySQL", e)

    def cerrar_conexion(self):
        if self.connection.is_connected():
            self.connection.close()                        
