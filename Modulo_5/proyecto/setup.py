import sqlite3

try:
    connection = sqlite3.connect("./bd/BaseDatosLocal3.db")
    sql_crear_table_query = """CREATE TABLE ventas (                              
                             id varchar(100) NULL,                                                     
                             descuento DOUBLE NULL,                                                     
                             total DOUBLE NULL,                                                     
                             propina DOUBLE NULL,                                                     
                             modo_pago DOUBLE NULL,                                                     
                             fecha_hora_venta DateTime NULL) """
    cursor = connection.cursor()
    result = cursor.execute(sql_crear_table_query)
    print("Creacion de tabla satisfactoiamente. ")
    cursor.close()
    connection.close()
except Exception as error:
    print(f"Fallo la creacion de la tabla: {error}")

try:
    connection = sqlite3.connect("./bd/BaseDatosLocal3.db")
    sql_crear_table_query = """CREATE TABLE ventas_servicio (                              
                             servicio varchar(100) NULL,                                                                                  
                             total DOUBLE NULL,                                                                                    
                             fecha_hora_venta DateTime NULL) """
    cursor = connection.cursor()
    result = cursor.execute(sql_crear_table_query)
    print("Creacion de tabla satisfactoiamente. ")
    cursor.close()
    connection.close()
except Exception as error:
    print(f"Fallo la creacion de la tabla: {error}")