import mysql.connector
from const.conf import HOST,DATABASE,USER,PASSWORD

try:
    connection = mysql.connector.connect(host=HOST,
                                                 database=DATABASE,
                                                 user=USER,
                                                 password=PASSWORD)
    #Tienda,Departamento,Fecha,Ventas_semanales,esvacaciones
    sql_crear_table_query = """CREATE TABLE ventas_semanales (                              
                             tienda int(11) NOT NULL,                                                     
                             departamento int(11) NOT NULL,                                                     
                             fecha Date NOT NULL,                                                     
                             ventas DOUBLE NOT NULL,                                                     
                             es_vacaciones int(11) NOT NULL) """

    cursor = connection.cursor()
    result = cursor.execute(sql_crear_table_query)
    print("Creacion de tabla satisfactoiamente. ")

except mysql.connector.Error as error:
    print(f"Fallo la creacion de la tabla en MySQL: {error}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexion cerrada")
