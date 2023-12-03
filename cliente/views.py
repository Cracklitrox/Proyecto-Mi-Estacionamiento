from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Cliente
from geolocalizacion.models import Puntointeres
from estacionamiento.models import *
from django.views import View
from django.http import JsonResponse
from arriendo.models import *
from arriendo.form import *

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

def registroCliente(request):
    return render(request,'registroCliente.html')

def loginCliente(request):
    if request.method == "POST":
        campoNombre = request.POST["campoNombre"]
        campoContrasena = request.POST["campoContrasena"]
        flagCorreo = False
        if campoNombre.endswith("@gmail.com"):
            flagCorreo = True
        try:
            if flagCorreo:
                cliente = Cliente.objects.get(
                    correoelectronico = campoNombre,
                    contrasena = campoContrasena
                )
            else:
                cliente = Cliente.objects.get(
                    nombreusuario = campoNombre,
                    contrasena = campoContrasena
                )
            user = authenticate(request, username=cliente.nombreusuario, password=campoContrasena)
            if user:
                login(request, user)
                return redirect('indexCliente')
        except Cliente.DoesNotExist:
            mensajeAdvertencia = "No se ha encontrado el nombre de usuario, correo o la contraseña. Por favor, inténtelo nuevamente."
            messages.warning(request, mensajeAdvertencia)
            return render(request, "loginCliente.html")
    else:
        return render(request, "loginCliente.html")
    

def estacionamientos(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, id=id)
    casilla = Casilla.objects.all()
    estacionamientoCasilla = EstacionamientoCasilla.objects.all()

    # Obtiene el id del dueño asociado al estacionamiento
    id_dueno_id = estacionamiento.id_dueno.id
    tarifahora = estacionamiento.tarifahora

    # Crea una instancia del formulario ArriendoForm
    arriendo_form = ArriendoForm(id_estacionamiento=id, id_dueno=id_dueno_id, preciototal=tarifahora)

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
        'estacionamientoCasilla': estacionamientoCasilla,
        'arriendo_form': arriendo_form,
    }

    return render(request, 'estacionamientos.html', context)

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