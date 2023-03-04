import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado a MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Tu estas conectado a la base de datos: ", record)

except Error as e:
    print("Error mientras se conectaba MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL cconexion esta cerrada")
