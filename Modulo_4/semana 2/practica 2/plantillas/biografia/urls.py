from django.urls import path
from . import views

urlpatterns = [          
    path('formulario', views.formulario, name='formulario'),           
]