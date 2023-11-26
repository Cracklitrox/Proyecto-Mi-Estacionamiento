from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from estacionamiento.models import *
from estacionamiento.forms import *
from geolocalizacion.models import *
from geolocalizacion.forms import *

# Create your views here.
def indexDueno(request):    
    estacionamientos = Estacionamiento.objects.all()
    return render(request,'indexDueno.html', {'estacionamientos':estacionamientos})

def cargando(request):
    casilla = Casilla.objects.all()
    context = {'casilla': casilla}
    return render(request,'cargando.html', context)

def addEstacionamiento(request):
    if request.method == 'POST':
        puntointeres_form = PuntointeresForm(request.POST)
        estacionamiento_form = EstacionamientoForm(request.POST)

        if estacionamiento_form.is_valid() and puntointeres_form.is_valid():
            puntointeres = puntointeres_form.save()
            estacionamiento = estacionamiento_form.save(commit=False)
            estacionamiento.id_puntoInteres = puntointeres
            estacionamiento.save()
            messages.success(request, 'Estacionamiento creado exitosamente.')
            return redirect('index')
        else:
            print(estacionamiento_form.errors)
            messages.error(request, 'Corrige los errores en el formulario.')

    else:
        puntointeres_form = PuntointeresForm()
        estacionamiento_form = EstacionamientoForm()

    return render(request, 'addEstacionamiento.html', {'puntointeres_form': puntointeres_form, 
                                                       'estacionamiento_form': estacionamiento_form})