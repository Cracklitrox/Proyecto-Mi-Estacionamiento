from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import BancoForm, TarjetacreditoForm, ComunaForm, ProvinciaForm, RegionForm, ContactoForm, ClienteForm, DuenoForm
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto
from cliente.models import Cliente
from dueno.models import Dueno


# Funciones BANCO
def agregarBanco(request):
    if request.method == 'POST':
        formulario = BancoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            formulario.full_clean()
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = BancoForm()
    return render(request, 'bancos/agregarBanco.html', {'form': formulario})

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
            messages.success(request, 'Banco modificado correctamente.')
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
    if request.method == 'POST':
        formulario = TarjetacreditoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = TarjetacreditoForm()
    return render(request, 'tarjetaCredito/agregarTarjetacredito.html', {'form': formulario})

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
            messages.success(request, 'Tarjeta de credito modificada correctamente.')
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
    if request.method == 'POST':
        formulario = ComunaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = ComunaForm()
    return render(request, 'comunas/agregarComuna.html', {'form': formulario})

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
            messages.success(request, 'Comuna modificado correctamente.')
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
    if request.method == 'POST':
        formulario = ProvinciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = ProvinciaForm()
    return render(request, 'provincias/agregarProvincia.html', {'form': formulario})

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
            messages.success(request, 'Provincia modificada correctamente.')
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
    if request.method == 'POST':
        formulario = RegionForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = RegionForm()
    return render(request, 'regiones/agregarRegion.html', {'form': formulario})

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
            messages.success(request, 'Region modificada correctamente.')
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
    if request.method == 'POST':
        formulario = ContactoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = ContactoForm()
    return render(request, 'contactos/agregarContacto.html', {'form': formulario})

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
            messages.success(request, 'Contacto modificado correctamente.')
            return redirect(to='listarContacto')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar el contacto."

    return render(request, 'contactos/modificarContacto.html', context)

def eliminarContacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect(to='listarContacto')


# Funciones CLIENTE


def agregarCliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = ClienteForm()
    return render(request, 'clientes/agregarCliente.html', {'form': formulario})

def listarCliente(request):
    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes
    }
    return render(request, 'clientes/listarCliente.html', context)

def modificarCliente(request, id):
    clientes = get_object_or_404(Cliente, id=id)

    context = {
        'form':ClienteForm(instance=clientes)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data = request.POST, instance=clientes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cliente modificado correctamente.')
            return redirect(to='listarCliente')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar el cliente."

    return render(request, 'clientes/modificarCliente.html', context)

def eliminarCliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect(to='listarCliente')


# Funciones DUENO

def agregarDueno(request):
    if request.method == 'POST':
        formulario = DuenoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': dict(formulario.errors)})
    else:
        formulario = DuenoForm()
    return render(request, 'duenos/agregarDueno.html', {'form': formulario})

def listarDueno(request):
    duenos = Dueno.objects.all()

    context = {
        'duenos': duenos
    }
    return render(request, 'duenos/listarDueno.html', context)

def modificarDueno(request, id):
    duenos = get_object_or_404(Dueno, id=id)

    context = {
        'form':DuenoForm(instance=duenos)
    }

    if request.method == 'POST':
        formulario = DuenoForm(data = request.POST, instance=duenos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listarDueno')
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido modificar el dueño."

    return render(request, 'duenos/modificarDueno.html', context)

def eliminarDueno(request, id):
    dueno = get_object_or_404(Dueno, id=id)
    dueno.delete()
    return redirect(to='listarDueno')