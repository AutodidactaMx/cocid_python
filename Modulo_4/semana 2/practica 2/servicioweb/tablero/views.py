import csv
from django.http import HttpResponse
from django.shortcuts import render
PATH_FILE = "./data/ventas.csv"

def obtener_info():
    with open(PATH_FILE, "r") as csvfile:
        reader_variable = csv.reader(csvfile, delimiter=",")
        next(reader_variable)
        
        result = [*map(lambda x: {
            "IdFactura": x[0],
            "Rama": x[1],
            "Ciudad": x[2],
            "TipoCliente": x[3],
            "Genero": x[4],
            "LineaDeProducto": x[5],
            "PrecioPorUnidad": x[6],
            "Cantidad": x[7],
            "Impuesto %5": x[8],
            "Total": x[9],
            "Fecha": x[10],
            "Hora": x[11],
            "Pago": x[12],
            "CostoDeBienes": x[13],
            "PorcentajeDeMagenBruto": x[14],
            "IngresosBrutos": x[15],
            "Clasificacion": x[16]
        }, reader_variable)]
    return result

def index(request):
    return HttpResponse("Hola soy tablero")

def formulario(request):     
    context = {
        "datos" :obtener_info() ,
    }
    datos = obtener_info()
    return render(request,"formtable.html",context)

