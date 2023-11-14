from django.shortcuts import render
from .models import Puntointeres

# Create your views here.

def gps(request):
    puntos_interes = Puntointeres.objects.all()

    # Pasa los puntos de interés a la plantilla
    return render(request, 'gps.html', {'puntos_interes': puntos_interes})
