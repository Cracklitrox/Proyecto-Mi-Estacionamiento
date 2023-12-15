from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db import connection
# CLIENTE
from .form import ClienteForm
# USUARIO
from usuario.forms import ClienteProfileForm
# ESTACIONAMIENTO
from estacionamiento.models import *
from estacionamiento.forms import VehiculoForm
# GEOLOCALIZACION
from geolocalizacion.forms import *
# ARRIENDO
from arriendo.models import Arriendo
from arriendo.form import *
# TRANSACCION_PAGO
from transaccion_pago.models import Tarjetacredito
from transaccion_pago.forms import TarjetacreditoForm

##################################
##        Grupo - permisos      ##
##################################

def in_cliente_group(user):
    return user.groups.filter(name__in=['Cliente']).exists()

##################################
##           Registro           ##
##################################


def registerCliente(request):
    if request.method == 'POST':
        user_form = ClienteForm(request.POST)
        profile_form = ClienteProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.es_cliente = True
            user.save()
            grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('loginCliente')
    else:
        user_form = ClienteForm()
        profile_form = ClienteProfileForm()
    
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'registration/registerCliente.html', context)


##################################
##            Login             ##
##################################

def loginCliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user.groups.filter(name='Cliente').exists():
                login(request, user)
                return redirect('indexCliente')
            else:
                messages.error(request, "No tienes permisos")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/loginCliente.html', {'form': form})


##################################
##            Logout            ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def logoutCliente(request):
    logout(request)
    # Personaliza la redirección para los dueños
    return redirect('indexCliente')

##################################
##            Index             ##
##################################

def indexCliente(request):
    if request.user.is_authenticated:
        id_usuario = request.user.id
        usuario = User.objects.get(id=id_usuario)
        estacionamientos = Estacionamiento.objects.all()
        puntos_interes = Puntointeres.objects.filter(id__in=estacionamientos.values('id_puntoInteres'))

        for estacionamiento in estacionamientos:
            estacionamiento.tarifahora_str = str(estacionamiento.tarifahora).replace(',', '.')

        context = {
            'usuario': usuario,
            'puntos_interes': puntos_interes,
            'estacionamientos': estacionamientos,
        }

        if not estacionamientos:
            # Si no hay estacionamientos, muestra un mensaje de advertencia
            messages.warning(request, 'No tienes estacionamientos. Agrega al menos uno para acceder a esta sección.')

        return render(request, 'indexCliente.html', context)
    else:
        puntos_interes = Puntointeres.objects.all()
        estacionamientos = Estacionamiento.objects.all()

        for estacionamiento in estacionamientos:
            estacionamiento.tarifahora_str = str(estacionamiento.tarifahora).replace(',', '.')

        context = {
            'puntos_interes': puntos_interes,
            'estacionamientos': estacionamientos,
        }
        return render(request, 'indexCliente.html', context)


##################################
##       Pago-Cliente           ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def pagoCliente(request):
    return render(request,'pagoCliente.html')


##################################
##           Arriendo           ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def estacionamientos(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, id=id)
    casillas = Casilla.objects.filter(id_estacionamiento=estacionamiento)

    # Obtiene el id del dueño asociado al estacionamiento
    id_usuario = request.user.id
    tarifahora = estacionamiento.tarifahora

    if request.method == 'POST':
        arriendo_form = ArriendoForm(request.POST, id_estacionamiento=id, id_user=id_usuario, preciototal=tarifahora)

        if arriendo_form.is_valid():
            arriendo = arriendo_form.save(commit=False)
            arriendo.save()

            
            messages.success(request, 'Arriendo creado exitosamente.')
            return redirect('indexCliente')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        arriendo_form = ArriendoForm(id_estacionamiento=id, id_user=id_usuario, preciototal=tarifahora)

    context = {
        'estacionamiento': estacionamiento,
        'casillas': casillas,
        'arriendo_form': arriendo_form,
    }

    return render(request, 'estacionamientos.html', context)

##################################
##   Función cambiar Casilla    ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def cambiar_casilla(request, casilla_id):
    try:
        casilla = Casilla.objects.get(id=casilla_id)
        casilla.cambiar_casilla()
        return JsonResponse({'estado': casilla.disponible})
    except Casilla.DoesNotExist:
        return JsonResponse({'error': 'casilla no encontrada'}, status=404)


##################################
##   Función guardar Casilla    ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
class GuardarEstadoCasillaView(View):
    def post(self, request, *args, **kwargs):
        id_casilla = request.POST.get('idCasilla')
        nuevo_estado = request.POST.get('nuevoEstado')

        # Actualiza el estado de la casilla en la base de datos
        casilla = Casilla.objects.get(id=id_casilla)
        casilla.disponible = nuevo_estado
        casilla.save()

        # Responde con un JSON para indicar el éxito de la operación si es necesario
        return JsonResponse({'success': True})
    

##################################
##      Listar-Arriendos        ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def listarArriendos(request):
    arriendos = Arriendo.objects.filter(id_user=request.user.id)
    mensaje = ''
    if not arriendos:
        mensaje = 'No puede ingresar a la página hasta arrendar al menos 1 estacionamiento'
    contexto = {'arriendos' : arriendos, 'mensaje': mensaje}
    return render(request, 'reserva/listarReserva.html', contexto)

##################################
##          Vehículos           ##
##################################

# Funciones Vehiculo

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def listarVehiculo(request):
    vehiculos = Vehiculo.objects.filter(id_usuario_id=request.user.id)
    context = {'vehiculos':vehiculos}
    return render(request, 'vehiculos/listarVehiculo.html', context)

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def agregarVehiculo(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            vehiculo = formulario.save(commit=False)
            vehiculo.id_usuario_id = request.user.id
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = VehiculoForm()
    return render(request, 'vehiculos/agregarVehiculo.html', {'form':formulario})

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def editarVehiculo(request, id):
    vehiculos = get_object_or_404(Vehiculo, id=id)
    context = {
        'form':VehiculoForm(instance=vehiculos)
    }
    if request.method == 'POST':
        formulario = VehiculoForm(data = request.POST, instance=vehiculos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Vehiculo modificado correctamente.')
            return redirect(to='listarVehiculo')
        else:
            context['form'] = formulario
    return render(request, 'vehiculos/editarVehiculo.html', context)

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def eliminarVehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    vehiculo.delete()
    return redirect(to='listarVehiculo')

##################################
##          Tarjetas            ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def listarTarjetacreditoCliente(request):
    tarjetascreditocliente = Tarjetacredito.objects.filter(id_usuario_id=request.user.id)
    context = {'tarjetas':tarjetascreditocliente}
    return render(request, 'tarjeta/listarTarjetacreditoCliente.html', context)

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def agregarTarjetacreditoCliente(request):
    if request.method == 'POST':
        formulario = TarjetacreditoForm(request.POST)
        if formulario.is_valid():
            tarjetacredito = formulario.save(commit=False)
            tarjetacredito.id_usuario_id = request.user.id
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = TarjetacreditoForm()
    return render(request, 'tarjeta/agregarTarjetacreditoCliente.html', {'form':formulario})


@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def editarTarjetacreditoCliente(request, id):
    tarjetas = get_object_or_404(Tarjetacredito, id=id)
    context = {
        'form':TarjetacreditoForm(instance=tarjetas)
    }
    if request.method == 'POST':
        formulario = TarjetacreditoForm(data = request.POST, instance=tarjetas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Tarjeta de Credito modificada correctamente.')
            return redirect(to='listarTarjetacreditoCliente')
        else:
            context['form'] = formulario
    return render(request, 'tarjeta/editarTarjetacreditoCliente.html', context)

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def eliminarTarjetacreditoCliente(request, id):
    tarjeta = get_object_or_404(Tarjetacredito, id=id)
    tarjeta.delete()
    return redirect(to='listarTarjetacreditoCliente')

##################################
##       Cambiar a Dueno        ##
##################################

@login_required(login_url="loginCliente")
@user_passes_test(in_cliente_group, login_url='loginCliente')
def cambiar_a_dueno(request):
    try:
        # Obtener el usuario actual
        user = request.user

        # Eliminar al usuario del grupo 'Cliente'
        grupo_cliente = Group.objects.get(name='Cliente')
        user.groups.remove(grupo_cliente)

        grupo_dueno, creado = Group.objects.get_or_create(name='Dueno')
        user.groups.add(grupo_dueno)

        user.save()
        return redirect('indexDueno')
    except Group.DoesNotExist:
        return HttpResponse("Error: Los grupos no están configurados correctamente. Contacta al administrador.")
    
def logout_dueno(request):
    user = request.user
    
    grupo_cliente = Group.objects.get(name='Cliente')
    user.groups.remove(grupo_cliente)

    grupo_dueno, creado = Group.objects.get_or_create(name='Dueno')
    user.groups.add(grupo_dueno)

    user.save()
    
    logout(request)
    
    # Personaliza la redirección para los dueños
    return redirect('loginDueno')


##################################
##          Notfounf            ##
##################################  
def notfound(request):
    return render(request, 'notfound.html')
