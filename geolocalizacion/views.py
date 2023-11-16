from django.shortcuts import render
from .models import *

# Create your views here.

def gps(request):
    puntos_interes = Puntointeres.objects.all()
    return render (request, 'gps.html', {'punto_intereses': puntos_interes})
