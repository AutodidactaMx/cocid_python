from django.http import HttpResponse, JsonResponse
from datetime import datetime


def saludos_espaniol(request):
    return HttpResponse("Saludos cordiales")

def saludos_dedicatoria(request):
    nombre = str(request.GET["nombre"])
    ciudad = str(request.GET["ciudad"])
    return HttpResponse(f"Saludos a mi estimado : {nombre} de la ciudad de {ciudad}")
    
def saludos_dedicatoria_especial(request,nombre,ciudad):    
    return HttpResponse(f"Saludos a mi estimado : {nombre} de la ciudad de {ciudad}")
    