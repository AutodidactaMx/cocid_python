import csv
from openpyxl import load_workbook
RUTA_ALMACENAMIENTO='./data/'

def guardar(nombre_archivo, datos):
    archivo = RUTA_ALMACENAMIENTO+nombre_archivo
    with open(archivo, 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        for cdr in datos:
            wr.writerow(list(cdr))

def leer(nombre_archivo):
    archivo = RUTA_ALMACENAMIENTO+nombre_archivo
    datos = []
    with open(archivo) as f:
        for line in f.readlines() : 
            for s in line.split(',') :
                datos.append(float(s))  
    return datos

def leerExcel(nombre_archivo,celda_ini, celda_fin):
    archivo = RUTA_ALMACENAMIENTO+nombre_archivo    
    wb = load_workbook(archivo)
    sheetH = wb.worksheets[0]
    datos = []
    cells = sheetH[celda_ini:celda_fin]
    for c1, in cells:
        datos.append(c1.value)
    return datos