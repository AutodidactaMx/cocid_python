from datetime import datetime
from modelos.modelo_venta import VentasSemanales
from PIL import ImageTk, Image

def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))  


def obtenerDatos(RUTA_DATOS):
    informacion = []
    with open((f"{RUTA_DATOS}"), mode="r", encoding="utf-8") as archivo:
        next(archivo)
        for line in archivo.readlines():
            fila = line.split(',')            
            obj = VentasSemanales(
                tienda=int(fila[0]),
                departamento=fila[1],
                fecha=datetime.strptime(fila[2], '%d/%m/%Y').date(),
                ventasSemanales=float(fila[3]),
                esVacaciones=bool(fila[4]))
            informacion.append(obj)
    return informacion


def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

def cm_to_pixel(value):
    return value/96

def porcentaje(numero,total):
    return 100 * float(numero) / float(total)