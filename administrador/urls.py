from django.urls import path
from . import views

urlpatterns = [
    # Paginas index_admin
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    # Pagina home_admin
    path('html/homeAdmin/', views.homeAdmin, name='homeAdmin'),
    # Paginas cliente
    path('cliente/panelCliente/', views.panelCliente, name='panelCliente'),
    path('cliente/crearCliente/', views.crearCliente, name='crearCliente'),
]