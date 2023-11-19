from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from estacionamiento.models import *
from estacionamiento.forms import *
from geolocalizacion.models import *
from geolocalizacion.forms import *

# Create your views here.
def indexDueno(request):
    return render(request,'indexDueno.html')

def cargando(request):
    return render(request,'cargando.html')

def estacionamientos(request):
    return render(request,'estacionamientos.html')

def addEstacionamiento(request):
    if request.method == 'POST':
        puntointeres_form = PuntointeresForm(request.POST)
        estacionamiento_form = EstacionamientoForm(request.POST)

        if puntointeres_form.is_valid():
            puntointeres = puntointeres_form.save()
            estacionamiento = estacionamiento_form.save(commit=False)
            estacionamiento.id_puntoInteres = puntointeres
            estacionamiento.save()
            # Puedes agregar más lógica aquí si es necesario

            return redirect('indexDueno')  # Reemplaza 'indexDueno' con el nombre de tu vista indexDueno
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        puntointeres_form = PuntointeresForm()
        estacionamiento_form = EstacionamientoForm()

    return render(request, 'addEstacionamiento.html', {'puntointeres_form': puntointeres_form, 
                                                       'estacionamiento_form': estacionamiento_form})