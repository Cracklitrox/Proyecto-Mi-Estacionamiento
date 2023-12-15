import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.db.models import F, ExpressionWrapper, fields, Avg, Count
from django.db.models.functions import Cast
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from django.http import HttpResponse
#Dueno
from .models import *
from .forms import *
#Arriendo
from arriendo.models import Arriendo
#Estacionamiento
from estacionamiento.models import *
from estacionamiento.forms import *
#Geolocalizacion
from geolocalizacion.models import *
from geolocalizacion.forms import *
# Usuario
from usuario.forms import UserForm, UsuarioProfileForm




##################################
##        Grupo - permisos      ##
##################################

def in_dueno_group(user):
    return user.groups.filter(name__in=['Dueno']).exists()

##################################
##           Registro           ##
##################################

def registerDueno(request):
    if request.method == 'POST':
        user_form = DuenoForm(request.POST)
        profile_form = UsuarioProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.es_dueno = True
            user.save()

            grupo_dueno, creado = Group.objects.get_or_create(name='Dueno')
            user.groups.add(grupo_dueno)
            grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            
            return redirect('loginDueno')  # Cambia esto según la ruta correcta
    else:
        user_form = DuenoForm()
        profile_form = UsuarioProfileForm()
    
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'registration/registerDueno.html', context)

##################################
##            Login             ##
##################################

def loginDueno(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.groups.filter(name='Dueno').exists():
                login(request, user)
                return redirect('indexDueno')
            else:
                messages.error(request, "No tienes permisos")
        else:
            messages.error(request, "Intentelo denuevo")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'registration/loginDueno.html', context)

##################################
##            Logout            ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
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
##           Index              ##
##################################


@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def indexDueno(request):    
    id = request.user.id
    estacionamientos = Estacionamiento.objects.filter(id_dueno=id)

    for estacionamiento in estacionamientos:
        casillas_estacionamiento = Casilla.objects.filter(id_estacionamiento=estacionamiento)
        estacionamiento.casillas_totales = casillas_estacionamiento.count()
        estacionamiento.casillas_disponibles = casillas_estacionamiento.filter(disponible=True).count()
        estacionamiento.casillas_ocupadas = casillas_estacionamiento.filter(disponible=False).count()

    puntos_interes = Puntointeres.objects.all()
    context = {'estacionamientos': estacionamientos, 
               'puntos_interes': puntos_interes }
    return render(request, 'indexDueno.html', context)

##################################
##      Add-Estacionamiento     ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def addEstacionamiento(request, id):
    dueno_profile = get_object_or_404(DuenoProfile, pk=id)
    if request.method == 'POST':
        puntointeres_form = PuntointeresForm(request.POST)
        estacionamiento_form = EstacionamientoForm(request.POST, files=request.FILES)

        if estacionamiento_form.is_valid() and puntointeres_form.is_valid():
            estacionamiento = estacionamiento_form.save(commit=False)
            estacionamiento.id_dueno = dueno_profile
            estacionamiento.disponible = True
            puntointeres = puntointeres_form.save()
            estacionamiento.id_puntoInteres = puntointeres
            estacionamiento.save()
            
            messages.success(request, 'Estacionamiento creado.')
            return redirect('indexDueno')
        else:
            print(estacionamiento_form.errors)
            messages.error(request, 'Corrige los errores en el formulario.')
            
    else:
        puntointeres_form = PuntointeresForm()
        estacionamiento_form = EstacionamientoForm()

    context= {'puntointeres_form' : puntointeres_form,
             'estacionamiento_form' : estacionamiento_form}

    return render(request, 'estacionamiento/addEstacionamiento.html', context)

##################################
##     Edit-Estacionamiento     ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def editEstacionamiento(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, id=id)
    punto_interes = estacionamiento.id_puntoInteres

    context = {
        'form': EstacionamientoForms(instance=estacionamiento),
        'punto_interes_form': PuntointeresForm(instance=punto_interes),
    }
    
    if request.method == 'POST':
        formulario = EstacionamientoForms(data= request.POST, instance=estacionamiento, files=request.FILES)
        punto_interes_form = PuntointeresForm(request.POST, instance=punto_interes)

        if formulario.is_valid() :
            # Guarda los cambios en el estacionamiento
            formulario.save()
            punto_interes_form.save()
            messages.success(request, 'Estacionamiento y Punto de Interés modificados.')
            return redirect(to='indexDueno')
        else:
            context["form"] = formulario
            context['punto_interes_form'] = punto_interes_form
            context["mensaje_incorrecto"] = "No se ha podido modificar el estacionamiento"

    return render(request, 'estacionamiento/editEstacionamiento.html', context)

   
##################################
##     Del-Estacionamiento      ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def eliminarEstacionamiento(request,id):
    estacionamiento = Estacionamiento.objects.get(id=id)
    estacionamiento.delete()
    return redirect('indexDueno')

##################################
##         Cambiar-Estado       ##
##################################
@csrf_exempt
@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def cambiar_estado(request, estacionamiento_id):
    try:
        estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
        estacionamiento.cambiar_estado()
        return JsonResponse({'estado': estacionamiento.disponible})
    except Estacionamiento.DoesNotExist:
        return JsonResponse({'error': 'Estacionamiento no encontrado'}, status=404)
    
##################################
##       Arriendo-list          ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def arriendo(request):
    arriendo_list = Arriendo.objects.all()
    estacionamientos = Estacionamiento.objects.filter(id_dueno=request.user.id)

    context = {
        'arriendo': arriendo_list,
        'estacionamientos': estacionamientos,
    }

    return render(request, 'estacionamiento/arriendo/arriendoDueno.html', context)



##################################
##       Generar-image          ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def link_callback(uri, rel):
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
        return path if os.path.isfile(path) else uri

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
        return path if os.path.isfile(path) else uri

    return uri

##################################
##       Generar-PDF            ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def generar_pdf(request, id_estacionamiento):
    try:
        # Obtén el usuario autenticado y el estacionamiento asociado
        id_usuario = request.user.id
        usuario = User.objects.get(id=id_usuario)
        estacionamiento = get_object_or_404(Estacionamiento, id=id_estacionamiento)
        arriendos = Arriendo.objects.filter(id_estacionamiento=estacionamiento)

        # Precio Total
        precio_total = sum(arriendo.preciototal for arriendo in arriendos)

        # Contador de estacionamientos
        arriendoTotal = arriendos.count()

        if arriendoTotal == 0:
            messages.warning(request, '')
            return redirect('listarArriendo')
        else:

            # Calcula la duración promedio en minutos
            duracion_promedio = arriendos.aggregate(
                promedio_duracion=Avg(F('horafin') - F('horainicio'))
            )['promedio_duracion']

            # Renderiza la plantilla HTML con el contexto
            template_path = 'estacionamiento/arriendo/pdf.html'
            context = {
                'usuario': usuario, 
                'estacionamiento': estacionamiento, 
                'arriendos': arriendos,  # Cambiado a 'arriendos'
                'precio_total': precio_total,
                'arriendoTotal': arriendoTotal,
                'duracion_promedio': duracion_promedio,
                'icon': os.path.join(settings.STATIC_URL, 'img/logo_mi_estacionamiento.jpg'),
            }
            template = get_template(template_path)
            html_content = template.render(context)

            # Configura la respuesta HTTP con el tipo de contenido y el nombre del archivo
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'filename="{usuario.username}_{estacionamiento.direccion}.pdf"'

            # Convierte la plantilla HTML a PDF y envía la respuesta
            pisa_status = pisa.CreatePDF(
                html_content, 
                dest=response,
                link_callback=link_callback)
            if pisa_status.err:
                return HttpResponse('Error al generar el PDF', status=500)
            return response
    
    except Exception as e:
        messages.error(request, f'Error al generar el PDF: {str(e)}')
        print(f'Error al generar el PDF: {str(e)}')
        return redirect('listarArriendo')


##################################
##       Dueno a Cliente        ##
##################################

@login_required(login_url="loginDueno")
@user_passes_test(in_dueno_group, login_url='loginDueno')
def cambiar_a_cliente(request):
    # Obtener el usuario actual
    user = request.user
    
    grupo_dueno = Group.objects.get(name='Dueno')
    user.groups.remove(grupo_dueno)
    
    grupo_cliente, creado = Group.objects.get_or_create(name='Cliente')
    user.groups.add(grupo_cliente)

    user.save()
    return redirect('indexCliente')