from django.urls import path

from . import views

urlpatterns = [          
    path('ventas', views.mostrar_formulario),        
    path('estilos', views.estilo_form),        
]
