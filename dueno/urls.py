from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from estacionamiento.views import cambiar_estado

urlpatterns = [
    #index
    path('indexDueno/',views.indexDueno,name='indexDueno'),
    #Registro
    path('registration/loginDueno/', views.loginDueno, name='loginDueno'),
    path('registration/registerDueno/', views.registerDueno, name='registerDueno'),
    path('logout_dueno/', views.logout_dueno, name='logoutDueno'),
    #Cambiar estado estacionamiento
    path('indexDueno/cambiar_estado/<int:estacionamiento_id>/', views.cambiar_estado, name='cambiar_estado'),
    #Cambiar a cliente
    path('cambiar-rol/', views.cambiar_rol, name='cambiar_rol'),
    #Estacionamiento
    path('indexDueno/addEstacionamiento/<int:id>',views.addEstacionamiento,name='addEstacionamiento'),
    path('eliminarEstacionamiento/<int:id>',views.eliminarEstacionamiento,name='eliminarEstacionamiento'),
    path('editEstacionamiento/<int:id>',views.editEstacionamiento,name='editEstacionamiento'),
    #Arriendo
    path('indexDueno/arriendo',views.arriendo, name="listarArriendo"),
    #PDF
    path('indexDueno/arriendo/pdf/<int:id_estacionamiento>', views.generar_pdf, name="generar_pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)