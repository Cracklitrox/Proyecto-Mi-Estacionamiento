from django.shortcuts import render
from geolocalizacion.models import Puntointeres
from estacionamiento.models import Estacionamiento

# Create your views here.
def indexCliente(request):
    puntos_interes = Puntointeres.objects.all()
    estacionamiento = Estacionamiento.objects.all()
    return render(request,'indexCliente.html', {'puntos_interes': puntos_interes,
                                                'estacionamiento': estacionamiento})

def pagoCliente(request):
    return render(request,'pagoCliente.html')

def registroCliente(request):
    
    return render(request,'registroCliente.html')