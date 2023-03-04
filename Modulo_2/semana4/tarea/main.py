import presentacion.presentacion as presentacion

import dominio.controlador.controlador_flujo as controlador


try:
    opcion = presentacion.presentacion_inicial()
    controlador.flujo(opcion)
    
except Exception as e:
    print("Existe un error : ", e)
