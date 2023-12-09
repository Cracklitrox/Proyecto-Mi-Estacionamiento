from django.urls import path, include
from . import views

urlpatterns = [
    # Ruta LOGUEO ADMINISTRADOR
    path('registration/login/', views.loginAdministrador, name='loginAdministrador'),
    path('registration/register/', views.registerAdministrador, name='registerAdministrador'),
    path('logout_admin/', views.logoutAdmin, name='logoutAdmin'),
    # Ruta PAGINA PRINCIPAL ADMINISTRADOR
    path('dashboard/', views.dashboard, name='dashboard'),
    # Rutas BANCOS
    path('bancos/agregarBanco/', views.agregarBanco, name='agregarBanco'),
    path('bancos/listarBanco/', views.listarBanco, name='listarBanco'),
    path('bancos/modificarBanco/<id>/', views.modificarBanco, name='modificarBanco'),
    path('bancos/eliminarBanco/<id>/', views.eliminarBanco, name='eliminarBanco'),
    # Rutas TARJETACREDITO
    path('tarjetaCredito/agregarTarjetacredito/', views.agregarTarjetacredito, name='agregarTarjetacredito'),
    path('tarjetaCredito/listarTarjetacredito/', views.listarTarjetacredito, name='listarTarjetacredito'),
    path('tarjetaCredito/modificarTarjetacredito/<id>/', views.modificarTarjetacredito, name='modificarTarjetacredito'),
    path('tarjetaCredito/eliminarTarjetacredito/<id>/', views.eliminarTarjetacredito, name='eliminarTarjetacredito'),
    # Rutas COMUNA
    path('comunas/agregarComuna/', views.agregarComuna, name='agregarComuna'),
    path('comunas/listarComuna/', views.listarComuna, name='listarComuna'),
    path('comunas/modificarComuna/<id>/', views.modificarComuna, name='modificarComuna'),
    path('comunas/eliminarComuna/<id>/', views.eliminarComuna, name='eliminarComuna'),
    # Rutas PROVINCIA
    path('provincias/agregarProvincia/', views.agregarProvincia, name='agregarProvincia'),
    path('provincias/listarProvincia/', views.listarProvincia, name='listarProvincia'),
    path('provincias/modificarProvincia/<id>/', views.modificarProvincia, name='modificarProvincia'),
    path('provincias/eliminarProvincia/<id>/', views.eliminarProvincia, name='eliminarProvincia'),
    # Rutas REGION
    path('regiones/agregarRegion/', views.agregarRegion, name='agregarRegion'),
    path('regiones/listarRegion/', views.listarRegion, name='listarRegion'),
    path('regiones/modificarRegion/<id>/', views.modificarRegion, name='modificarRegion'),
    path('regiones/eliminarRegion/<id>/', views.eliminarRegion, name='eliminarRegion'),
    # Rutas CONTACTO
    path('contactos/agregarContacto/', views.agregarContacto, name='agregarContacto'),
    path('contactos/listarContacto/', views.listarContacto, name='listarContacto'),
    path('contactos/modificarContacto/<id>/', views.modificarContacto, name='modificarContacto'),
    path('contactos/eliminarContacto/<id>/', views.eliminarContacto, name='eliminarContacto'),
#     # Rutas CLIENTE
#     path('clientes/agregarCliente/', views.agregarCliente, name='agregarCliente'),
#     path('clientes/listarCliente/', views.listarCliente, name='listarCliente'),
#     path('clientes/modificarCliente/<id>/', views.modificarCliente, name='modificarCliente'),
#     path('clientes/eliminarCliente/<id>/', views.eliminarCliente, name='eliminarCliente'),
#     # Rutas DUENO
#     path('duenos/agregarDueno/', views.agregarDueno, name='agregarDueno'),
#     path('duenos/listarDueno/', views.listarDueno, name='listarDueno'),
#     path('duenos/modificarCliente/<id>/', views.modificarDueno, name='modificarDueno'),
#     path('duenos/eliminarDueno/<id>/', views.eliminarDueno, name='eliminarDueno'),
]