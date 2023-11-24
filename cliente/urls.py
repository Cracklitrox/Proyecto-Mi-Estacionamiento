from django.urls import path
from . import views
from geolocalizacion.models import *

urlpatterns = [
    path('',views.indexCliente,name='indexCliente'),
    path('indexCliente/',views.indexCliente,name='indexCliente'),
    path('pagoCliente/',views.pagoCliente,name='pagoCliente'),
    path('registroCliente/',views.registroCliente,name='registroCliente'),
    path('loginCliente/', views.loginCliente, name='loginCliente'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]