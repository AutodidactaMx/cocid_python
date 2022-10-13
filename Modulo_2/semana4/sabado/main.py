from tratamiento.proceso import *

while(True):
    try :        
        print("""
        0) Salir
        1) CargaDatos
        2) Ventas por departamento
        3) Ventas por tienda
        4) Ventas por tienda        
        """)
        opcion = int(input("Elije el proceso a ejecutar : "))
        if opcion == 1:
            CargaDatos()
        elif opcion == 2:
            ProcesoVentasDepartameto()
        elif opcion == 3:
            ProcesoVentasTienda()
        elif opcion == 4:
            ProcesoVentasAnio()
        elif opcion == 0:
            break
    except ValueError as e:
        print("Solo acepta opciones 1,2,3 : ")
    except Exception as e:
        print(e)
