from django.shortcuts import render, redirect, get_object_or_404
from .forms import BancoForm, TarjetacreditoForm, ComunaForm, ProvinciaForm, RegionForm, ContactoForm
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto


# Funciones BANCO

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


# Funciones TARJETACREDITO


def agregarTarjetacredito(request):
    context = {
        'form':TarjetacreditoForm()
    }

    if request.method == 'POST':
        formulario = TarjetacreditoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Tarjeta de credito guardada."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar la tarjeta de credito."
    return render(request, 'tarjetaCredito/agregarTarjetacredito.html', context)

def listarTarjetacredito(request):
    tarjetacreditos = Tarjetacredito.objects.all()

    context = {
        'tarjetacreditos': tarjetacreditos
    }
    return render(request, 'tarjetaCredito/listarTarjetacredito.html', context)

def modificarTarjetacredito(request, id):
    tarjetacredito = get_object_or_404(Tarjetacredito, id=id)

    context = {
        'form':TarjetacreditoForm(instance=tarjetacredito)
    }

    if request.method == 'POST':
        formulario = TarjetacreditoForm(data = request.POST, instance=tarjetacredito)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarTarjetacredito')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar la tarjeta de credito."

    return render(request, 'tarjetaCredito/modificarTarjetacredito.html', context)

def eliminarTarjetacredito(request, id):
    tarjetacredito = get_object_or_404(Tarjetacredito, id=id)
    tarjetacredito.delete()
    return redirect(to='listarTarjetacredito')


# Funciones COMUNA


def agregarComuna(request):
    context = {
        'form':ComunaForm
    }

    if request.method == 'POST':
        formulario = ComunaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Comuna guardada."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar la comuna."
    return render(request, 'comunas/agregarComuna.html', context)

def listarComuna(request):
    comunas = Comuna.objects.all()

    context = {
        'comunas': comunas
    }
    return render(request, 'comunas/listarComuna.html', context)

def modificarComuna(request, id):
    comunas = get_object_or_404(Comuna, id=id)

    context = {
        'form':ComunaForm(instance=comunas)
    }

    if request.method == 'POST':
        formulario = ComunaForm(data = request.POST, instance=comunas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarComuna')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar la comuna."

    return render(request, 'comunas/modificarComuna.html', context)

def eliminarComuna(request, id):
    comuna = get_object_or_404(Comuna, id=id)
    comuna.delete()
    return redirect(to='listarComuna')


# Funciones PROVINCIA


def agregarProvincia(request):
    context = {
        'form':ProvinciaForm
    }
    if request.method == 'POST':
        formulario = ProvinciaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Provincia guardada."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar la provincia."
    return render(request, 'provincias/agregarProvincia.html', context)

def listarProvincia(request):
    provincias = Provincia.objects.all()

    context = {
        'provincias': provincias
    }
    return render(request, 'provincias/listarProvincia.html', context)

def modificarProvincia(request, id):
    provincias = get_object_or_404(Provincia, id=id)

    context = {
        'form':ProvinciaForm(instance=provincias)
    }

    if request.method == 'POST':
        formulario = ProvinciaForm(data = request.POST, instance=provincias)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarProvincia')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar la provincia."

    return render(request, 'provincias/modificarProvincia.html', context)

def eliminarProvincia(request, id):
    provincia = get_object_or_404(Provincia, id=id)
    provincia.delete()
    return redirect(to='listarProvincia')


# Funciones REGION


def agregarRegion(request):
    context = {
        'form':RegionForm
    }

    if request.method == 'POST':
        formulario = RegionForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Region guardada."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar la region."
    return render(request, 'regiones/agregarRegion.html', context)

def listarRegion(request):
    regiones = Region.objects.all()

    context = {
        'regiones': regiones
    }
    return render(request, 'regiones/listarRegion.html', context)

def modificarRegion(request, id):
    regiones = get_object_or_404(Region, id=id)

    context = {
        'form':RegionForm(instance=regiones)
    }

    if request.method == 'POST':
        formulario = RegionForm(data = request.POST, instance=regiones)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarRegion')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar la region."

    return render(request, 'regiones/modificarRegion.html', context)

def eliminarRegion(request, id):
    region = get_object_or_404(Region, id=id)
    region.delete()
    return redirect(to='listarRegion')


# Funciones CONTACTO


def agregarContacto(request):
    context = {
        'form':ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Contacto guardado."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido guardar el contacto."
    return render(request, 'contactos/agregarContacto.html', context)

def listarContacto(request):
    contactos = Contacto.objects.all()

    context = {
        'contactos': contactos
    }
    return render(request, 'contactos/listarContacto.html', context)

def modificarContacto(request, id):
    contactos = get_object_or_404(Contacto, id=id)

    context = {
        'form':ContactoForm(instance=contactos)
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST, instance=contactos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarContacto')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar el contacto."

    return render(request, 'contactos/modificarContacto.html', context)

def eliminarContacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect(to='listarContacto')