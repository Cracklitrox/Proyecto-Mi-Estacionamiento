from django.shortcuts import render, redirect
from .models import Administrador
from cliente.models import Cliente
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna


# Funcion del formulario en la pagina 'index_admin'
def indexAdmin(request):
    if request.method == "POST":
        campoNombre = request.POST["campoNombre"]
        campoContrasena = request.POST["campoContrasena"]
        flagCorreo = False
        if campoNombre.endswith("@gmail.com"):
            flagCorreo = True
        try:
            if flagCorreo:
                administrador = Administrador.objects.get(
                    correoelectronico=campoNombre, contrasena=campoContrasena
                )
            else:
                administrador = Administrador.objects.get(
                    nombreusuario=campoNombre, contrasena=campoContrasena
                )
            request.session["id"] = administrador.id
            request.session["nivelPermiso"] = administrador.nivelpermiso
            request.session["estadoEmpleo"] = administrador.estadoempleo
            return redirect("homeAdmin")
        except Administrador.DoesNotExist:
            mensajeAdvertencia = "No se ha encontrado el nombre de usuario, correo o la contraseña. Por favor, intentelo nuevamente."
            return render(
                request, "indexAdmin.html", {"mensajeAdvertencia": mensajeAdvertencia}
            )
    else:
        return render(request, "indexAdmin.html")


# Funcion para verificar permisos
def verificarPermisos(request):
    nivelPermiso = request.session.get("nivelPermiso")
    if nivelPermiso is None:
        mensajeLogueo = "Usted no tiene permisos para acceder al siguiente sitio, por favor inicie sesión."
        return render(request, "indexAdmin.html", {"mensajeLogueo": mensajeLogueo})
    else:
        idAdministrador = request.session.get("id")
        administrador = Administrador.objects.get(id=idAdministrador)
        nombreUsuario = administrador.nombreusuario
        return nombreUsuario


# Funcion para verificar los niveles de permisos
def verificarPermisosAdministrador(request, nivelPermiso, vistaFuncion, context=None):
    nombreUsuario = verificarPermisos(request)
    if nombreUsuario is None:
        return redirect("indexAdmin")
    else:
        nivelPermisoAdministrador = request.session.get("nivelPermiso")
        try:
            administrador = Administrador.objects.get(id=request.session.get("id"))
        except Administrador.DoesNotExist:
            administrador = None

        if nivelPermisoAdministrador == nivelPermiso:
            return (
                vistaFuncion(request, context)
                if context is not None
                else vistaFuncion(request)
            )
        else:
            nombreUsuarioAdministrador = (
                administrador.nombreusuario if administrador else ""
            )
            mensajePermisos = "Lo siento, no tiene permisos para acceder al siguiente modelo, por favor consulte con su administrador principal."
            return render(
                request,
                "html/homeAdmin.html",
                {
                    "mensajePermisos": mensajePermisos,
                    "nombreUsuarioAdministrador": nombreUsuarioAdministrador,
                },
            )


# Funcion para cerrar sesion
def cerrarSesion(request):
    del request.session["id"]
    del request.session["nivelPermiso"]
    del request.session["estadoEmpleo"]
    return render(request, "indexAdmin.html")


# Funcion para redireccionar al usuario a la pagina 'homeAdmin'
def homeAdmin(request):
    nombreUsuarioAdministrador = verificarPermisos(request)
    return render(
        request,
        "html/homeAdmin.html",
        {"nombreUsuarioAdministrador": nombreUsuarioAdministrador},
    )


# Funciones Cliente
# Funcion para mostrar los Clientes
def panelCliente(request):
    def panelClienteInner(request):
        cliente = Cliente.objects.all()
        context = {"cliente": cliente}
        return render(request, "html/cliente/panelCliente.html", context)

    idAdministrador = request.session.get("id")
    administrador = Administrador.objects.get(id=idAdministrador)
    administradorPermiso = administrador.nivelpermiso
    if administradorPermiso == 2 or administradorPermiso == 3:
        return verificarPermisosAdministrador(
            request, administradorPermiso, panelClienteInner
        )
    else:
        return verificarPermisosAdministrador(
            request, 3, "html/homeAdmin.html", panelClienteInner
        )

def obtener_lista_bancos():
    bancos = Banco.objects.all()
    return bancos

def obtener_lista_comunas():
    comunas = Comuna.objects.all()
    return comunas

def crearCliente(request):
    def crearClienteInner(request):
        if request.method == "POST":
            runCliente = request.POST["runCliente"].strip()
            dv_runCliente = request.POST["dv_runCliente"].strip()
            pnombreCliente = request.POST["pnombreCliente"].strip()
            snombreCliente = request.POST["snombreCliente"].strip()
            appnombreCliente = request.POST["appnombreCliente"].strip()
            apmnombreCliente = request.POST["apmnombreCliente"].strip()
            correoElectronicoCliente = request.POST["correoElectronicoCliente"].strip()
            telefonoCliente = request.POST["telefonoCliente"].strip()
            nombreUsuarioCliente = request.POST["nombreUsuarioCliente"].strip()
            contrasenaCliente = request.POST["contrasenaCliente"].strip()
            confirmarContrasenaCliente = request.POST["confirmarContrasenaCliente"].strip()
            direccionCliente = request.POST["direccionCliente"].strip()
            numeroTarjetaCliente = request.POST["numeroTarjetaCliente"].strip()
            fechaVencimientoTarjetaCliente = request.POST["fechaVencimientoTarjetaCliente"].strip()
            cvvTarjetaCliente = request.POST["cvvTarjetaCliente"].strip()
            idBancoCliente = request.POST["idBancoCliente"].strip()
            idComuna = request.POST["idComuna"].strip()
            if not (runCliente 
                    and dv_runCliente 
                    and pnombreCliente 
                    and snombreCliente 
                    and appnombreCliente 
                    and apmnombreCliente 
                    and correoElectronicoCliente 
                    and telefonoCliente 
                    and nombreUsuarioCliente 
                    and contrasenaCliente 
                    and confirmarContrasenaCliente 
                    and direccionCliente 
                    and numeroTarjetaCliente 
                    and fechaVencimientoTarjetaCliente 
                    and cvvTarjetaCliente 
                    and idBancoCliente 
                    and idComuna):
                context = {'mensajeCreacionCliente':'❌ Error: Todos los campos son obligatorios'}
            elif contrasenaCliente == confirmarContrasenaCliente:
                if Cliente.objects.filter(run = runCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: El run ingresado ya está en uso'}
                elif Cliente.objects.filter(correoelectronico = correoElectronicoCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: El correo ingresado ya está en uso'}
                elif Cliente.objects.filter(telefono = telefonoCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: El telefono ingresado ya está en uso'}
                elif Cliente.objects.filter(nombreusuario = nombreUsuarioCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: El nombre de usuario ingresado ya está en uso'}
                elif Cliente.objects.filter(contrasena = contrasenaCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: La contraseña ingresada ya está en uso'}
                elif Tarjetacredito.objects.filter(numero = numeroTarjetaCliente).exists():
                    context = {'mensajeCreacionCliente':'❌ Error: La tarjeta ingresada ya pertenece a otro usuario'}
                else:
                    if len(runCliente) != 8:
                        context = {'mensajeCreacionCliente': '❌ Error: El run del cliente debe tener 8 valores numericos.'}
                    elif len(pnombreCliente) < 3 and len(pnombreCliente) > 30:
                        context = {'mensajeCreacionCliente':'❌ Error: El primer nombre del cliente debe ser mayor a 3 caracteres y menor a 30 caracteres.'}
                    elif len(snombreCliente) < 3 and len(snombreCliente) > 30:
                        context = {'mensajeCreacionCliente':'❌ Error: El segundo nombre del cliente debe ser mayor a 3 caracteres y menor a 30 caracteres.'}
                    elif len(appnombreCliente) < 3 and len(appnombreCliente) > 30:
                        context = {'mensajeCreacionCliente':'❌ Error: El apellido paterno del cliente debe ser mayor a 3 caracteres y menor a 50 caracteres.'}
                    elif len(apmnombreCliente) < 3 and len(apmnombreCliente) > 30:
                        context = {'mensajeCreacionCliente':'❌ Error: El apellido materno del cliente debe ser mayor a 3 caracteres y menor a 50 caracteres.'}
                    elif len(correoElectronicoCliente) < 5 and len(correoElectronicoCliente) > 65:
                        context = {'mensajeCreacionCliente':'❌ Error: El correo electronico del cliente debe ser mayor a 5 caracteres y menor a 65 caracteres.'}
                    elif len(telefonoCliente) != 9:
                        context = {'mensajeCreacionCliente':'❌ Error: El telefono del cliente debe ser contener un total de 9 numeros.'}
                    elif len(nombreUsuarioCliente) < 3 and len(nombreUsuarioCliente) > 20:
                        context = {'mensajeCreacionCliente':'❌ Error: El nombre de usuario del cliente debe ser mayor a 3 caracteres y menor a 20 caracteres.'}
                    elif len(contrasenaCliente) < 3 and len(contrasenaCliente) > 20:
                        context = {'mensajeCreacionCliente':'❌ Error: La contraseña del cliente debe ser mayor a 3 caracteres y menor a 30 caracteres.'}
                    elif len(direccionCliente) < 5:
                        context = {'mensajeCreacionCliente':'❌ Error: La direccion del cliente debe ser mayor a 5 caracteres.'}
                    elif len(numeroTarjetaCliente) < 12 and len(contrasenaCliente) > 19:
                        context = {'mensajeCreacionCliente':'❌ Error: El numero de la tarjeta del cliente debe ser mayor a 12 caracteres y menor a 19 caracteres.'}
                    elif len(fechaVencimientoTarjetaCliente) == 0:
                        context = {'mensajeCreacionCliente':'❌ Error: La fecha de vencimiento de la tarjeta del cliente no puede estar vacia.'}
                    elif len(cvvTarjetaCliente) != 3:
                        context = {'mensajeCreacionCliente':'❌ Error: El "CVV" de la tarjeta del cliente debe tener solo 3 numeros.'}
                    elif len(contrasenaCliente) < 3 and len(contrasenaCliente) > 20:
                        context = {'mensajeCreacionCliente':'❌ Error: La contraseña del cliente debe ser mayor a 3 caracteres y menor a 30 caracteres.'}
                    else:
                        camposTarjeta = {
                            "numero" : numeroTarjetaCliente,
                            "fechavencimiento" : fechaVencimientoTarjetaCliente,
                            "cvv" : cvvTarjetaCliente
                        }
                        Tarjetacredito.objects.create(**camposTarjeta)
                        if Tarjetacredito.objects.filter(numero=numeroTarjetaCliente).exists():
                            tarjeta_credito = Tarjetacredito.objects.get(numero=numeroTarjetaCliente)
                            idTarjetaCredito = tarjeta_credito
                        else:
                            idTarjetaCredito = None
                        banco = Banco.objects.get(id=idBancoCliente)
                        idBanco = banco

                        comuna = Comuna.objects.get(id=idComuna)
                        idComunaCliente = comuna
                        camposCliente = {
                            "run" : runCliente,
                            "dv_run" : dv_runCliente,
                            "pnombre" : pnombreCliente,
                            "snombre" : snombreCliente,
                            "appaterno" : appnombreCliente,
                            "apmaterno" : apmnombreCliente,
                            "correoelectronico" : correoElectronicoCliente,
                            "telefono" : telefonoCliente,
                            "nombreusuario" : nombreUsuarioCliente,
                            "contrasena" : contrasenaCliente,
                            "direccion" : direccionCliente,
                            "id_tarjetacredito" : idTarjetaCredito,
                            "id_banco" : idBanco,
                            "id_comuna" : idComunaCliente
                        }
                        cliente = Cliente.objects.create(**camposCliente)
                        context = {'mensajeCreacionCliente':'✔ Cliente creado con éxito', 'cliente':cliente}
            else:   
                context = {'mensajeCreacionCliente':'❌ Error: Las contraseñas deben ser iguales'}
            return render(request, 'html/cliente/crearCliente.html', context)
        else:
            context = {
                'bancos': obtener_lista_bancos(),
                'comunas': obtener_lista_comunas(),
            }
            return render(request, 'html/cliente/crearCliente.html', context)
    idAdministrador = request.session.get('id')
    administrador = Administrador.objects.get(id = idAdministrador)
    administradorPermiso = administrador.nivelpermiso
    if administradorPermiso == 2 or administradorPermiso == 3:
        return verificarPermisosAdministrador(request, administradorPermiso, crearClienteInner)
    else:
        return verificarPermisosAdministrador(request, 3, 'html/homeAdmin.html', crearClienteInner)