from django.urls import path
from . import views

urlpatterns = [ 
    path('lista', views.lista),       
    path('form', views.crear_venta),   
    path('mensaje', views.mensaje),    
    path('<str:id>/eliminar', views.eliminar), 
]