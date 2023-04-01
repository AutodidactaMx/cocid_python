import mysql.connector
from persistencia.env import HOST,DATABASE,USER,PASSWORD

class RepositorioConexion:
    connection: any

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
