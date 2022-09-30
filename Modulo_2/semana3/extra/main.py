from const.conf import RUTA_DATOS
from mod.ssn import Sismicidad
from mod.excepciones import MagnitudApocaliticaError, RangoError
from mod.validacion import *

def obtenerDatos():
    informacion_sismo = []
    with open((f"{RUTA_DATOS}/Sismicidad.csv"), mode="r", encoding="utf-8") as archivo:
        next(archivo)
        for line in archivo.readlines() : 
            fila = line.split('|')
            informacion_sismo.append(Sismicidad(magnitud=float(fila[0]),epicentro=fila[1],profundidad=fila[2]))
    return informacion_sismo

def solicitarDatos():
    print("Busqueda informacion de sismo por rango de magnitud")
    magnitud_ini = input("Introduce la magnitud de inicial:")
    magnitud_final = input("Introduce la magnitud de final:")
    return float(magnitud_ini), float(magnitud_final) 

try : 
    filtro = []
    magnitud_rango = solicitarDatos()
    validarMagnitudMaxima(magnitud_rango)
    validarRangoCorrecto(magnitud_rango)
    for sismicidad in obtenerDatos():
            if sismicidad.magnitud>=magnitud_rango[0] and sismicidad.magnitud<=magnitud_rango[1] :
                filtro.append(sismicidad)

    for info in filtro:
            print(info.magnitud ,info.epicentro, " " ,info.profundidad,end="\n")
except ValueError:  
  print("Lo siento no es valor numerico")
except RangoError as e:
    print(e.mensaje)
except MagnitudApocaliticaError as e:
    print(e.mensaje)
except:
  print("Es un error generico")