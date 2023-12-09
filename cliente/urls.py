from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
#from .views import GuardarEstadoCasillaView
from geolocalizacion.models import *
from estacionamiento.views import *


urlpatterns = [
    path('',views.indexCliente,name='indexCliente'),
    path('registration/loginCliente/', views.loginCliente, name='loginCliente'),
    path('registration/registerCliente/', views.registerCliente, name='registerCliente'),
    path('logout_cliente/', views.logoutCliente, name='logoutCliente'),
    path('indexCliente/',views.indexCliente,name='indexCliente'),
    path('pagoCliente/',views.pagoCliente,name='pagoCliente'),
    path('indexCliente/estacionamientos/<int:id>/',views.estacionamientos,name='estacionamientos'),
    #path('indexCliente/estacionamientos/cambiar_casilla/<int:casilla_id>',cambiar_casilla,name='cambiar_casilla'),
    #path('guardar_estado/', GuardarEstadoCasillaView.as_view(), name='guardar_estado'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]