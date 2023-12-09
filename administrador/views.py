from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from .forms import BancoForm, TarjetacreditoForm, ComunaForm, ProvinciaForm, RegionForm, ContactoForm
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto
from .forms import AdministradorForm


def registerAdministrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('loginAdministrador')
            else:
                messages.error(request, 'La autenticación ha fallado.')
        else:
            messages.error(request, 'El formulario no es válido.')
    else:
        form = AdministradorForm()
    return render(request, 'registration/registerAdministrador.html', {'form': form})

def loginAdministrador(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Nombre de administrador o contraseña no válidos.')
    return render(request, 'registration/loginAdministrador.html')


# Funcion PAGINA PRINCIPAL
def dashboard(request):
    return render(request, 'dashboard.html')

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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(bancos, 5)
        bancos = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': bancos,
        'paginator': paginator
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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(tarjetacreditos, 5)
        tarjetacreditos = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': tarjetacreditos,
        'paginator': paginator
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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(comunas, 5)
        comunas = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': comunas,
        'paginator': paginator
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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(provincias, 5)
        provincias = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': provincias,
        'paginator': paginator
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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(regiones, 5)
        regiones = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': regiones,
        'paginator': paginator
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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(contactos, 5)
        contactos = paginator.page(page)
    except:
        raise Http404
    context = {
        'entity': contactos,
        'paginator': paginator
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