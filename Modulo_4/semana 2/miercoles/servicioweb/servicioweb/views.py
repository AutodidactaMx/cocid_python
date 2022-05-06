import csv
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

def obtener_info_filtrada(columna, valor):
    result = obtener_info()
    return list(filter(lambda item: item[columna] == valor, result))


def fecha_hora_actual(request):
    now = datetime.now().strftime("%b %d %Y - %H:%M hrs ")
    return HttpResponse(f"Fecha hora actual del servidor {str(now)}")

def obtener_info_total(request):
    datos = obtener_info()
    return JsonResponse(datos, safe=False)

def obtener_info_columna(request, columna, valor):
    datos = obtener_info_filtrada(columna, valor)
    return JsonResponse(datos, safe=False)
    
@csrf_exempt
def save_events_json(request):    
    if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')                        
            body = json.loads(body_unicode)
            content = body['CuentaUsuario']
            d = 0
    return HttpResponse("OK")
