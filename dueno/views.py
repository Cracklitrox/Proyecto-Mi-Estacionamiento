from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from estacionamiento.models import *
from estacionamiento.forms import *
from geolocalizacion.models import *
from geolocalizacion.forms import *
from usuario.forms import UsuarioRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.

# Funcion REGISTRO DUEÑO

def registerDueno(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.es_dueno = True
            user.save()
            return redirect('loginCliente')
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'registration/registerDueno.html', {'form': form})

def loginDueno(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/loginDueno.html', {'form': form})

# FUnciones que faltan nombrar

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


def editEstacionamiento(request, id=id):
    estacionamiento = Estacionamiento.objects.get(id=id)
    formulario = EstacionamientoForm(request.POST or None,request.FILES or None,instance=estacionamiento)
    return render(request,'editEstacionamiento.html', {'formulario':formulario})

def eliminarEstacionamiento(request,id):
    estacionamiento = Estacionamiento.objects.get(id=id)
    estacionamiento.delete()
    return redirect('index')