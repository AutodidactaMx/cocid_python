import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')

    sql_crear_table_query = """CREATE TABLE persona ( 
                             id int(11) NOT NULL,
                             nombre varchar(250) NOT NULL,                                                     
                             PRIMARY KEY (id)) """

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
