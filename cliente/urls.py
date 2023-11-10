from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('pago/',views.pago,name='pago'),
    path('registro/',views.registro,name='registro'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]