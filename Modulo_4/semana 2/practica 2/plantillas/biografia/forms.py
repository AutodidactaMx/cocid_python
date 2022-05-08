from unicodedata import name
from django import forms
from django.core.exceptions import ValidationError
import re
def validar_exclucion_numeros(value):
    if value != 'None':
        numeros =  re.sub("[^0-9]", "", value)
        if numeros:
            raise ValidationError("No permite numeros")
        else:
            return value
    return value

class FormPersonalizado(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100,required=True)
    apellido = forms.CharField(label='Apellido', max_length=100)
    usuario = forms.CharField(label='Usuario', max_length=5)
    ciudad = forms.CharField(label='Ciudad', max_length=100,validators =[validar_exclucion_numeros])        
    
    def __init__(self, *args, **kwargs):
        super(FormPersonalizado, self).__init__(*args, **kwargs)        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
                    