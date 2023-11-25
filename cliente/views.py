from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Cliente
from geolocalizacion.models import Puntointeres
from estacionamiento.models import Estacionamiento
from arriendo.models import *
from arriendo.form import *

# Create your views here.
def indexCliente(request):
    puntos_interes = Puntointeres.objects.all()
    estacionamiento = Estacionamiento.objects.all()
    context = {
        'puntos_interes': puntos_interes,
        'estacionamiento': estacionamiento
        }
    return render(request,'indexCliente.html', context)

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

def estacionamientos(request):
    context = {
        
        }
    return render(request,'estacionamientos.html',context )