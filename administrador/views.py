from django.shortcuts import render
from .forms import BancoForm
from transaccion_pago.models import Banco

# Create your views here.

def agregarBanco(request):
    context = {
        'form':BancoForm()
    }

    if request.method == 'POST':
        formulario = BancoForm(data = request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Banco guardado."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar el banco."
    return render(request, 'bancos/agregarBanco.html', context)

def listarBanco(request):
    bancos = Banco.objects.all()

    context = {
        'bancos': bancos
    }
    return render(request, 'bancos/listarBanco.html', context)