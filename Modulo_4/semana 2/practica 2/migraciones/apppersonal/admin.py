from django.contrib import admin

# Register your models here.
from .models  import Persona,TipoEmpleado

class PersonaAdmin(admin.ModelAdmin):
    fieldsets = (        
        ('Informacion basica', {
            'fields': ('rfc','nombre_completo')
        }),
        ('Datos generales', {
            'fields': ('direccion','tipo_empleado','es_empleado','edad','altura','cintura')
        }),
        ('Datos empresa', {
            'fields': ('fecha_registro','sueldo')
        }),
    )    
    list_display = ('rfc','nombre_completo','direccion')
    list_display_links = ('rfc','nombre_completo')
    list_editable = ('direccion',)
    list_filter = ('nombre_completo',)
    search_fields = ('rfc',)
class TipoEmpleadoAdmin(admin.ModelAdmin):
    
    fields = ['descripcion']
    list_display = ('id','descripcion')
    list_display_links = ('id',)
    list_editable = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)
    
admin.site.register(Persona,PersonaAdmin)
admin.site.register(TipoEmpleado,TipoEmpleadoAdmin)