from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from estacionamiento.models import *
from django.views import View
from django.http import JsonResponse

from geolocalizacion.forms import *
from arriendo.models import *
from arriendo.form import *
from .forms import ClienteForm
from .models import Cliente

def registerCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginCliente')
    else:
        form = ClienteForm()
    return render(request, 'registration/registerCliente.html', {'form':form})

def loginCliente(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']
        cliente = Cliente.objects.filter(nombre_usuario=nombre_usuario).first()
        if cliente is not None and cliente.check_password(contrasena):
            login(request, cliente)
            return redirect('indexCliente')
    return render(request, 'registration/loginCliente.html')


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

def pagoCliente(request):
    return render(request,'pagoCliente.html')


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