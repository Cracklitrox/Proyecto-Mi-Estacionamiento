from django.urls import path
from . import views
from estacionamiento.views import cambiar_estado

urlpatterns = [
    path('index/',views.indexDueno,name='index'),
    path('index/cambiar_estado/<int:estacionamiento_id>/', cambiar_estado, name='cambiar_estado'),
    path('cargando/',views.cargando,name='cargando'),
    path('index/addEstacionamiento/',views.addEstacionamiento,name='addEstacionamiento'),
    path('eliminarEstacionamiento/<int:id>',views.eliminarEstacionamiento,name='eliminarEstacionamiento'),
    path('editEstacionamiento/<int:id>',views.editEstacionamiento,name='editEstacionamiento'),


]