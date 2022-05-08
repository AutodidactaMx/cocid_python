from django.db import models
from datetime import datetime
# Create your models here.
class TipoEmpleado(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)  

class Persona(models.Model):
    rfc = models.CharField(
        primary_key=True, max_length=100, null=False)
    nombre_completo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100,null=True)
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.SET_NULL, null=True)
    es_empleado = models.BooleanField(default=False)
    edad = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(default=datetime.now())
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    altura = models.FloatField(null=True)
    cintura =  models.TextField(null=True)

  