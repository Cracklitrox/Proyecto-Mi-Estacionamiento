from django.shortcuts import render, redirect
from .models import Administrador

# Funcion del formulario en la pagina 'index_admin'
def indexAdmin(request):
    if request.method == 'POST':
        campoNombre = request.POST['campoNombre'];
        campoContrasena = request.POST['campoContrasena'];
        flagCorreo = False;
        if campoNombre.endswith('@gmail.com'):
            flagCorreo = True;
        try:
            if flagCorreo:
                administrador = Administrador.objects.get(correoelectronico = campoNombre, contrasena = campoContrasena)
            else :
                administrador = Administrador.objects.get(nombreusuario = campoNombre, contrasena = campoContrasena)
            request.session['id'] = administrador.id
            request.session['nivelPermiso'] = administrador.nivelpermiso
            request.session['estadoEmpleo'] = administrador.estadoempleo
            return redirect('homeAdmin')
        except Administrador.DoesNotExist:
            mensajeAdvertencia = 'No se ha encontrado el nombre de usuario, correo o la contraseña. Por favor, intentelo nuevamente.'
            return render(request, 'indexAdmin.html', {'mensajeAdvertencia':mensajeAdvertencia})
    else:
        return render(request, 'indexAdmin.html')

# Funcion para verificar permisos
def verificarPermisos(request):
    nivelPermiso = request.session.get('nivelPermiso')
    if nivelPermiso is None:
        mensajeLogueo = 'Usted no tiene permisos para acceder al siguiente sitio, por favor inicie sesión.'
        return render(request, 'indexAdmin.html', {'mensajeLogueo': mensajeLogueo})
    else:
        idAdministrador = request.session.get('id')
        administrador = Administrador.objects.get(id = idAdministrador)
        nombreUsuario = administrador.nombreusuario
        return nombreUsuario

# Funcion para verificar los niveles de permisos
def verificarPermisosAdministrador(request, nivelPermiso, vistaFuncion):
    nombreUsuario = verificarPermisos(request)
    if nombreUsuario is None:
        return redirect('indexAdmin')
    else:
        nivelPermisoAdministrador = request.session.get('nivelPermiso')
        if nivelPermisoAdministrador == nivelPermiso:
            return vistaFuncion(request)
        else:
            idAdministrador = request.session.get('id')
            administrador = Administrador.objects.get(id = idAdministrador)
            nombreUsuarioAdministrador = administrador.nombreusuario
            mensajePermisos = 'Lo siento, no tiene permisos para acceder al siguiente modelo, por favor consulte con su administrador principal.'
            return render(request, 'html/homeAdmin.html', {'mensajePermisos':mensajePermisos, 'nombreUsuarioAdministrador':nombreUsuarioAdministrador})

# Funcion para cerrar sesion
def cerrarSesion(request):
    del request.session['id']
    del request.session['nivelPermiso']
    del request.session['estadoEmpleo']
    return render(request, 'indexAdmin.html')

def homeAdmin(request):
    nombreUsuarioAdministrador = verificarPermisos(request)
    return render(request, 'html/homeAdmin.html', {'nombreUsuarioAdministrador': nombreUsuarioAdministrador})