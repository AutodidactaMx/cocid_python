from django.db import models

# Create your models here.
 
class Ventas(models.Model):
    id_factura = models.CharField(
        primary_key=True, max_length=100,  null=False)
    rama = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo_cliente = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    linea_de_producto = models.CharField(max_length=100)
    precio_por_unidad = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_hora = models.DateTimeField() 
    


