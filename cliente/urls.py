from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#from .views import GuardarEstadoCasillaView
from geolocalizacion.models import *
from estacionamiento.views import *
from arriendo.models import *
from arriendo.models import Arriendo
from arriendo.views import *



urlpatterns = [
    #Index
    path('',views.indexCliente,name='indexCliente'),
    path('indexCliente/',views.indexCliente,name='indexCliente'),
    #Registro 
    path('registration/loginCliente/', views.loginCliente, name='loginCliente'),
    path('registration/registerCliente/', views.registerCliente, name='registerCliente'),
    path('logout_cliente/', views.logoutCliente, name='logoutCliente'),
    #Arriendo
    path('indexCliente/listar/',views.listarArriendos,name='listar'),
    #Vehículos
    path('indexCliente/tarjetaCliente/',views.tarjetaCliente,name='tarjeta'),
     #Tarjetas
    path('indexCliente/vehiculosCliente/',views.vehiculosCliente,name='vehiculos'),

    path('pagoCliente/',views.pagoCliente,name='pagoCliente'),
    #Estacionamiento / Arriendo
    path('indexCliente/estacionamientos/<int:id>/',views.estacionamientos,name='estacionamientos'),

    #path('indexCliente/estacionamientos/cambiar_casilla/<int:casilla_id>',cambiar_casilla,name='cambiar_casilla'),
    #path('guardar_estado/', GuardarEstadoCasillaView.as_view(), name='guardar_estado'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]