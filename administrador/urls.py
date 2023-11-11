from django.urls import path
from . import views

urlpatterns = [
    # Paginas index_admin
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    # Pagina home_admin
    path('html/homeAdmin/', views.homeAdmin, name='homeAdmin')
]