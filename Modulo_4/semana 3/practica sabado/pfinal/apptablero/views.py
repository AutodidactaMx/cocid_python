from django.shortcuts import render
from .models import Ventas
from django.db.models import Count, Sum
from datetime import datetime

def content_date_time_column_chart():
    labels, data = [], []
    queryset = (Ventas.objects.values('fecha', 'hora', 'total'))
    for venta in queryset:
        labels.append( str(datetime.combine(venta['fecha'], venta['hora'])))
        data.append(float(venta['total']))
    return {
        'labels': labels,
        'data': data,
    }


def content_total_filter_chart(column_filter, column_sum):
    labels, data = [], []
    queryset = (Ventas.objects.values(column_filter)
                ).annotate(total=Sum(column_sum))
    for venta in queryset:
        labels.append(venta[column_filter])
        data.append(float(venta['total']))
    return {
        'labels': labels,
        'data': data,
    }


def tablero(request):

    context = {
        "pie_city": content_total_filter_chart(column_filter="ciudad", column_sum="total"),
        "dought_gender": content_total_filter_chart(column_filter="genero", column_sum="total"),
        "bar_pay": content_total_filter_chart(column_filter="pago", column_sum="total"),
        "line_pay" : content_date_time_column_chart()


    }

    return render(request, 'tablero.html', context)
