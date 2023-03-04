from mod.excepciones import MagnitudApocaliticaError, RangoError

def validarMagnitudMaxima(magnitud_rango):
    if magnitud_rango[0]>10 :
       raise MagnitudApocaliticaError

def validarRangoCorrecto(magnitud_rango):
    if magnitud_rango[0]>magnitud_rango[1] :
       raise RangoError   
