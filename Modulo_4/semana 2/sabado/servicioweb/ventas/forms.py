from unicodedata import name
from django import forms

class FormVentas(forms.Form):
    id_factura = forms.CharField(label='Id de factura', max_length=100)
    rama = forms.CharField(label='rama', max_length=100)
    ciudad = forms.CharField(label='ciudad', max_length=100)
    tipo_cliente = forms.CharField(label='tipo_cliente', max_length=100)
    genero = forms.CharField(label='genero', max_length=100)
    linea_de_producto = forms.CharField(label='linea_de_producto', max_length=100)
    precio_por_unidad = forms.CharField(label='precio_por_unidad', max_length=100)
    cantidad = forms.CharField(label='cantidad', max_length=100)
    impuesto = forms.CharField(label='impuesto', max_length=100)
    total = forms.CharField(label='total', max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(FormVentas, self).__init__(*args, **kwargs)        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
                    