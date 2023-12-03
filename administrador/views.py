from django.shortcuts import render, redirect, get_object_or_404
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

def modificarBanco(request, id):
    banco = get_object_or_404(Banco, id=id)

    context = {
        'form':BancoForm(instance=banco)
    }

    if request.method == 'POST':
        formulario = BancoForm(data = request.POST, instance=banco, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarBanco')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar el banco."

    return render(request, 'bancos/modificarBanco.html', context)

def eliminarBanco(request, id):
    banco = get_object_or_404(Banco, id=id)
    banco.delete()
    return redirect(to='listarBanco')