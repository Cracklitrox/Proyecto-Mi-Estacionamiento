from django.shortcuts import render
<<<<<<< HEAD
from .models import Puntointeres
=======
from .models import *
>>>>>>> 696b6bebebad010afbad8985f0e55eccbfb5d77e

# Create your views here.

def gps(request):
    puntos_interes = Puntointeres.objects.all()
<<<<<<< HEAD

    # Pasa los puntos de interés a la plantilla
    return render(request, 'gps.html', {'puntos_interes': puntos_interes})
=======
    return render (request, 'gps.html', {'punto_intereses': puntos_interes})
>>>>>>> 696b6bebebad010afbad8985f0e55eccbfb5d77e
