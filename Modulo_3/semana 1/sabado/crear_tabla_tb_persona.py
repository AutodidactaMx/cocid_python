import mysql.connector
from persistencia.env import HOST,DATABASE,USER,PASSWORD

try:
    connection = mysql.connector.connect(host=HOST,
                                                 database=DATABASE,
                                                 user=USER,
                                                 password=PASSWORD)
    #Tienda,Departamento,Fecha,Ventas_semanales,esvacaciones
    sql_crear_table_query = """CREATE TABLE tb_persona (                              
                             curp varchar(100),                                                     
                             nombre varchar(100),                                                     
                             edad varchar(100),                                                     
                             correo varchar(100),                                                     
                             telefono varchar(100) )"""

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
