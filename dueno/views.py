from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import JsonResponse
#Dueno
from .models import *
from .forms import *
#Estacionamiento
from estacionamiento.models import *
from estacionamiento.forms import *
#Geolocalizacion
from geolocalizacion.models import *
from geolocalizacion.forms import *
# Usuario
from usuario.forms import UserForm, UsuarioProfileForm



##################################
##        Grupo - permisos      ##
##################################

def es_dueno(user):
    return user.groups.filter(name='Dueno').exists()

##################################
##           Registro           ##
##################################

def registerDueno(request):
    if request.method == 'POST':
        user_form = DuenoForm(request.POST)
        profile_form = UsuarioProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.es_dueno = True
            user.save()

            grupo_dueno, creado = Group.objects.get_or_create(name='Dueno')
            user.groups.add(grupo_dueno)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            
            return redirect('loginDueno')  # Cambia esto según la ruta correcta

    else:
        user_form = DuenoForm()
        profile_form = UsuarioProfileForm()
    
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'registration/registerDueno.html', context)

##################################
##            Login             ##
##################################
def loginDueno(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.groups.filter(name='Dueno').exists():
                login(request, user)
                return redirect('indexDueno')
            else:
                messages.error(request, "No tienes permisos")
        else:
            messages.error(request, "Intentelo denuevo")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'registration/loginDueno.html', context)

##################################
##            Logout            ##
##################################
@user_passes_test(es_dueno)
def logout_dueno(request):
    logout(request)
    # Personaliza la redirección para los dueños
    return redirect('loginDueno')

##################################
##           Index              ##
##################################

@user_passes_test(es_dueno)
def indexDueno(request):    
    estacionamientos = Estacionamiento.objects.all()
    context = {'estacionamientos':estacionamientos}
    return render(request,'indexDueno.html', context)

def cargando(request):
    casilla = Casilla.objects.all()
    context = {'casilla': casilla}
    return render(request,'cargando.html', context)

##################################
##      Add-Estacionamiento     ##
##################################

@user_passes_test(es_dueno)
def addEstacionamiento(request, id):
    dueno_profile = get_object_or_404(DuenoProfile, pk=id)
    if request.method == 'POST':
        puntointeres_form = PuntointeresForm(request.POST)
        estacionamiento_form = EstacionamientoForm(request.POST)

        if estacionamiento_form.is_valid() and puntointeres_form.is_valid():
            estacionamiento = estacionamiento_form.save(commit=False)
            puntointeres = puntointeres_form.save()
            estacionamiento.id_dueno = dueno_profile
            estacionamiento.id_puntoInteres = puntointeres
            estacionamiento.save()
            messages.success(request, 'Estacionamiento creado exitosamente.')
            return redirect('indexDueno')
        else:
            print(estacionamiento_form.errors)
            messages.error(request, 'Corrige los errores en el formulario.')
            
    else:
        puntointeres_form = PuntointeresForm()
        estacionamiento_form = EstacionamientoForm()

    context= {'puntointeres_form' : puntointeres_form,
             'estacionamiento_form' : estacionamiento_form}

    return render(request, 'addEstacionamiento.html', context)

##################################
##     Edit-Estacionamiento     ##
##################################

@user_passes_test(es_dueno)
def editEstacionamiento(request, id=id):
    estacionamiento = Estacionamiento.objects.get(id=id)
    formulario = EstacionamientoForm(request.POST or None,request.FILES or None,instance=estacionamiento)
    return render(request,'editEstacionamiento.html', {'formulario':formulario})

##################################
##     Del-Estacionamiento      ##
##################################

@user_passes_test(es_dueno)
def eliminarEstacionamiento(request,id):
    estacionamiento = Estacionamiento.objects.get(id=id)
    estacionamiento.delete()
    return redirect('index')

##################################
##         Cambiar-Estado       ##
##################################
@csrf_exempt
@user_passes_test(es_dueno)
def cambiar_estado(request, estacionamiento_id):
    try:
        estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
        estacionamiento.cambiar_estado()
        return JsonResponse({'estado': estacionamiento.disponible})
    except Estacionamiento.DoesNotExist:
        return JsonResponse({'error': 'Estacionamiento no encontrado'}, status=404)