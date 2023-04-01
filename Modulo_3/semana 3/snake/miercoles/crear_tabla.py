import sqlite3

try:
    connection = sqlite3.connect("./bd/BaseDatosLocal3.db")
    sql_crear_table_query = """CREATE TABLE ventas_semanales (                              
                             tienda int(11) NOT NULL,                                                     
                             departamento int(11) NOT NULL,                                                     
                             fecha Date NOT NULL,                                                     
                             ventas DOUBLE NOT NULL,                                                     
                             es_vacaciones int(11) NOT NULL) """
    cursor = connection.cursor()
    result = cursor.execute(sql_crear_table_query)
    print("Creacion de tabla satisfactoiamente. ")
    cursor.close()
    connection.close()
except Exception as error:
    print(f"Fallo la creacion de la tabla: {error}")