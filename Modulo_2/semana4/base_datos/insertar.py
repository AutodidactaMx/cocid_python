import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')

    mySql_insert_query = """INSERT into 
    persona (id, nombre) VALUES (1, 'Datos') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Fue registrado satisfactoriamente")
    cursor.close()

except mysql.connector.Error as error:
    print(f"Fallo la insercion {error}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL conexion cerrada")
