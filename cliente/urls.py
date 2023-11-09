from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    #path('html/cartelera/',views.cartelera,name='cartelera'),
    #path('html/index/',views.index, name="index"),
]