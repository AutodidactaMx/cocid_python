from django.shortcuts import render
from . import forms
# Create your views here.

def formulario(request):
    contexto = {"estado":""}
    if request.method == 'POST':        
        form = forms.FormPersonalizado(request.POST)        
        if form.is_valid():
            nombre = form.cleaned_data['nombre'] 
            apellido = form.cleaned_data['apellido'] 
            ciudad = form.cleaned_data['ciudad'] 
            usuario = form.cleaned_data['usuario'] 
            contexto["estado"] = "success"
    else:
        form = forms.FormPersonalizado()

    return render(request,"formulario.html",{'form': form,'contexto':contexto})    
