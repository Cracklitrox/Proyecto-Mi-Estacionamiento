from django.urls import path
from . import views

urlpatterns = [
    path('bancos/agregarBanco/', views.agregarBanco, name='agregarBanco'),
    path('bancos/listarBanco/', views.listarBanco, name='listarBanco'),
    path('bancos/modificarBanco/<id>/', views.modificarBanco, name='modificarBanco'),
    path('bancos/eliminarBanco/<id>/', views.eliminarBanco, name='eliminarBanco')
]