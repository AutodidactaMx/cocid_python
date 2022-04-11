from django.http import HttpResponse, JsonResponse
from datetime import datetime

def hola_mundo(request):
    now = datetime.now().strftime("%b %d %Y - %H:%M hrs ")
    return HttpResponse(f"Current server time {str(now)}")

def hola_mundo_json(request):
    lista = str(request.GET["numeros"]).split(',')
    dicionario = {}
    for idx, x in enumerate(lista):
        dicionario[idx] = x
    data = {
        "status": "ok",
        "numeros": dicionario,
        "mensaje": "success"
    }
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
def info(request,nombre,edad):
    content = f"""
    <!DOCTYPE html>
    <html>
    <body style="background-color:powderblue;">

    <h1>Hola {nombre}</h1>
    <p>Tu edad es {edad}</p>

    </body>
    </html>
    """
    return HttpResponse(content)