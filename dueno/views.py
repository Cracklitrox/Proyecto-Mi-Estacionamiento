from django.shortcuts import render
from .models import *

# Create your views here.
def indexDueno(request):
    return render(request,'indexDueno.html')

def cargando(request):
    return render(request,'cargando.html')

def estacionamientos(request):
    return render(request,'estacionamientos.html')

def addEstacionamiento(request):
    puntos_interes = Puntointeres.objects.all()
    return render(request, 'addEstacionamiento.html',{'puntos_interes':puntos_interes})