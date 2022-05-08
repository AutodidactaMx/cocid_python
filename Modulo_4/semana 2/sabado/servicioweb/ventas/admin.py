from django.contrib import admin


# Register your models here.
from .models import Ventas

class VentasAdmin(admin.ModelAdmin):
    #fields = ['id_factura','ciudad', 'rama','tipo_cliente','genero','linea_de_producto','precio_por_unidad','cantidad','impuesto','total','fecha_hora']    
    list_display = ('id_factura','ciudad', 'rama','tipo_cliente','genero','linea_de_producto','precio_por_unidad','cantidad','impuesto','total','fecha_hora')
    list_display_links = ('id_factura', )
    list_editable = ('fecha_hora',)
    list_filter = ('ciudad', 'rama')
    search_fields = ('id_factura','ciudad')
    fieldsets = (
        ('Clave', {
            'fields': ('id_factura',)
        }),
        ('General', {
            'fields': ('ciudad', 'rama','tipo_cliente','genero','linea_de_producto','fecha_hora',)
        }),
        ('Costos', {
            'fields': ('precio_por_unidad','cantidad','impuesto','total',)
        }),
    )

admin.site.register(Ventas, VentasAdmin)