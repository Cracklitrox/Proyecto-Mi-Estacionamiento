from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from estacionamiento.views import cambiar_estado

urlpatterns = [
    path('indexDueno/',views.indexDueno,name='indexDueno'),
    path('registration/loginDueno/', views.loginDueno, name='loginDueno'),
    path('registration/registerDueno/', views.registerDueno, name='registerDueno'),
    path('logout_dueno/', views.logout_dueno, name='logoutDueno'),
    path('indexDueno/cambiar_estado/<int:estacionamiento_id>/', views.cambiar_estado, name='cambiar_estado'),
    path('cargando/',views.cargando,name='cargando'),
    path('indexDueno/addEstacionamiento/<int:id>',views.addEstacionamiento,name='addEstacionamiento'),
    path('eliminarEstacionamiento/<int:id>',views.eliminarEstacionamiento,name='eliminarEstacionamiento'),
    path('editEstacionamiento/<int:id>',views.editEstacionamiento,name='editEstacionamiento'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)