import mysql.connector

try:
    connection = mysql.connector.connect(host='proweb-corp.com',
                                         database='prowebco_cocid',
                                         user='prowebco_alumnos_cocid',
                                         password='qpF5n,QDotkU')

    sql_select_Query = "select * from persona"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total de numero de registros en la tabla: ", cursor.rowcount)

    print("\nImprimiendo cada registro")
    for row in records:
        print("id = ", row[0], )
        print("nombre = ", row[1])

except mysql.connector.Error as e:
    print("Error al leer los datos de la tabla MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL conexion cerrada")
