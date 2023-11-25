from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexDueno,name='indexDueno'),
    path('indexDueno/',views.indexDueno,name='indexDueno'),
    path('cargando/',views.cargando,name='cargando'),
    path('estacionamientos/',views.estacionamientos,name='estacionamientos'),
    path('addEstacionamiento/',views.addEstacionamiento,name='addEstacionamiento'),
    path('eliminarEstacionamiento/<int:id>',views.eliminarEstacionamiento,name='eliminarEstacionamiento'),
    path('editEstacionamiento/<int:id>',views.editEstacionamiento,name='editEstacionamiento'),

]