from django.urls import path
from . import views

urlpatterns = [
    path('',views.gps,name='gps'),
    path('gps/',views.gps,name='gps'),
]