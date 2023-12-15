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
from dueno.views import *


urlpatterns = [
    path('',views.indexCliente,name='indexCliente'),
    path('indexCliente/',views.indexCliente,name='indexCliente'),
    #Registro 
    path('registration/loginCliente/', views.loginCliente, name='loginCliente'),
    path('registration/registerCliente/', views.registerCliente, name='registerCliente'),
    path('logout_cliente/', views.logoutCliente, name='logoutCliente'),
    #Cambiar rol
    path('cambiar_a_dueno', views.cambiar_a_dueno, name='cambiar_a_dueno'),
    path('logoutDueno', views.logout_dueno, name='logoutDueno2'),
    #Arriendo
    path('indexCliente/listar/',views.listarArriendos,name='listar'),
    # Rutas VEHICULOS
    path('vehiculos/listarVehiculo/', views.listarVehiculo, name='listarVehiculo'),
    path('vehiculos/agregarVehiculo/', views.agregarVehiculo, name='agregarVehiculo'),
    path('vehiculos/editarVehiculo/<id>/', views.editarVehiculo, name='editarVehiculo'),
    path('vehiculos/eliminarVehiculo/<id>/', views.eliminarVehiculo, name='eliminarVehiculo'),
    # Rutas TARJETA
    path('tarjeta/listarTarjetacreditoCliente/',views.listarTarjetacreditoCliente,name='listarTarjetacreditoCliente'),
    path('tarjeta/agregarTarjetacreditoCliente/', views.agregarTarjetacreditoCliente, name='agregarTarjetacreditoCliente'),
    path('tarjeta/editarTarjetacreditoCliente/<id>/', views.editarTarjetacreditoCliente, name='editarTarjetacreditoCliente'),
    path('tarjeta/eliminarTarjetacreditoCliente/<id>/', views.eliminarTarjetacreditoCliente, name='eliminarTarjetacreditoCliente'),

    #Not Found 
    path('notfound/',views.notfound,name='notfound'),

    #Pago Cliente
    path('pagoCliente/',views.pagoCliente,name='pagoCliente'),
        
    #Estacionamiento / Arriendo
    path('indexCliente/estacionamientos/<int:id>/',views.estacionamientos,name='estacionamientos'),
    path('indexCliente/estacionamientos/cambiar_casilla/<int:casilla_id>',views.cambiar_casilla,name='cambiar_casilla'),
    #path('guardar_estado/', GuardarEstadoCasillaView.as_view(), name='guardar_estado'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]