from django.contrib import admin
from .models import Ventas

class VentasAdmin(admin.ModelAdmin):
    fieldsets = (        
        ('Folio de referencia', {
            'fields': ('id_factura',)
        }),
        ('Datos generales', {
            'fields': ('rama','ciudad','tipo_cliente','genero','linea_de_producto')
        }),
        ('Datos venta', {
            'fields': ('precio_por_unidad','cantida','impuesto','total','fecha','hora','pago','costo_de_bienes','porcentaje_de_magen_bruto','ingresos_brutos','clasificacion')
        }),
    )    
    list_display = ('id_factura','rama','ciudad','tipo_cliente','genero','linea_de_producto','precio_por_unidad','cantida','impuesto','total','fecha','hora','pago','costo_de_bienes','porcentaje_de_magen_bruto','ingresos_brutos','clasificacion')
    list_display_links = ('id_factura',)    
    list_filter = ('ciudad','genero','linea_de_producto')
    search_fields = ('ciudad',)

admin.site.register(Ventas,VentasAdmin)
