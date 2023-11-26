from django.urls import path
from . import views
from estacionamiento.views import cambiar_estado
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/',views.indexDueno,name='index'),
    path('index/cambiar_estado/<int:estacionamiento_id>/', cambiar_estado, name='cambiar_estado'),
    path('cargando/',views.cargando,name='cargando'),
    path('index/addEstacionamiento/',views.addEstacionamiento,name='addEstacionamiento'),
    path('eliminarEstacionamiento/<int:id>',views.eliminarEstacionamiento,name='eliminarEstacionamiento'),
    path('editEstacionamiento/<int:id>',views.editEstacionamiento,name='editEstacionamiento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)