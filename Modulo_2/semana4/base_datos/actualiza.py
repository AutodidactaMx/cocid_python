import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')
    cursor = connection.cursor()

    print("Antes de actualizar el registro ")
    sql_select_query = """select * from persona where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update persona set nombre = 'cambio' where id = 1"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Actualizacion de registro satisfactorio")

    print("Despues de la actualizacion de registro")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Fallo la actualizacion del registro: {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL conexion cerrada")
