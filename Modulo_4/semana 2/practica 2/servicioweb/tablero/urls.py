from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),    
    path('ventas', views.formulario),    
]
