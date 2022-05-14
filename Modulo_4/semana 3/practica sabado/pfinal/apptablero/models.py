from django.db import models
# Create your models here.


class Ventas(models.Model):
    id_factura = models.CharField(
        primary_key=True, max_length=100, null=False)
    rama = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo_cliente = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    linea_de_producto = models.CharField(max_length=100)
    precio_por_unidad = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    cantida = models.IntegerField(default=0)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    pago = models.CharField(max_length=100)
    costo_de_bienes = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    porcentaje_de_magen_bruto = models.FloatField(null=True)
    ingresos_brutos = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    clasificacion = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
