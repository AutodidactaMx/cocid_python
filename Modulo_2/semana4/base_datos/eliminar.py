import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    cursor = connection.cursor()
    print("La tabla antes de ser eliminado el registro")
    sql_select_query = """select * from persona where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Delete a record
    sql_Delete_query = """Delete from persona where id = 1"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('numero de registro eliminado', cursor.rowcount)

    # Verify using select query (optional)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Registro eliminado satisfactoriamente ")

except mysql.connector.Error as error:
    print("Fallor la eliminacion de registro de la tabla: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexion cerrada")
