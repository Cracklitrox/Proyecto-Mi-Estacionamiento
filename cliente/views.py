from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
# Cliente
from .form import ClienteForm
# Usuario
from usuario.forms import UserForm
#Estacionamiento
from estacionamiento.models import *
#Geolocalizacion
from geolocalizacion.forms import *
#Arriendo
from arriendo.models import *
from arriendo.form import *

##################################
##        Grupo - permisos      ##
##################################

# def es_cliente(user):
#     return user.groups.filter(name='Cliente').exists()  

##################################
##           Registro           ##
##################################


def registerCliente(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        #profile_form = ClienteForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.es_cliente = True
            user.save()
            grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #profile.save()
            return redirect('loginCliente')
    else:
        user_form = UserForm()
        #profile_form = ClienteForm()
    return render(request, 'registration/registerCliente.html', {'user_form': user_form})

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
def logoutCliente(request):
    logout(request)
    # Personaliza la redirección para los dueños
    return redirect('indexCliente')


# Create your views here.
def indexCliente(request):
    puntos_interes = Puntointeres.objects.all()
    estacionamientos = Estacionamiento.objects.all()

    for estacionamiento in estacionamientos:
        estacionamiento.tarifahora_str = str(estacionamiento.tarifahora).replace(',', '.')

    context = {
        'puntos_interes': puntos_interes,
        'estacionamientos': estacionamientos,
    }
    return render(request, 'indexCliente.html', context)


@login_required(login_url="loginCliente")
def pagoCliente(request):
    return render(request,'pagoCliente.html')

@login_required(login_url="loginCliente")
def estacionamientos(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, id=id)
    casilla = Casilla.objects.all()
    # estacionamientoCasilla = EstacionamientoCasilla.objects.all()

    # Obtiene el id del dueño asociado al estacionamiento
    id_usuario = estacionamiento.id
    tarifahora = estacionamiento.tarifahora

    # Crea una instancia del formulario ArriendoForm
    arriendo_form = ArriendoForm(id_estacionamiento=id, id_usuario=id, preciototal=tarifahora)

    if request.method == 'POST':
        # Procesar el formulario cuando se envíe
        arriendo_form = ArriendoForm(request.POST)

        if arriendo_form.is_valid():
            # Guarda el formulario y realiza las acciones necesarias
            arriendo = arriendo_form.save(commit=False)
            arriendo.save()

            # Resto del código para actualizar las casillas...
            
            messages.success(request, 'Estacionamiento creado exitosamente.')
            return redirect('indexCliente')
        else:
            print(arriendo_form.errors)
            messages.error(request, 'Corrige los errores en el formulario.')

    # Método GET, renderiza la página con el formulario
    context = {
        'estacionamiento': estacionamiento,
        'casilla': casilla,
        'arriendo_form': arriendo_form,
    }

    return render(request, 'estacionamientos.html', context)

@login_required(login_url="loginCliente")
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