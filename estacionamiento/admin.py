from django.contrib import admin
from .models import Vehiculo, DuenoVehiculo, Estacionamiento, ClienteVehiculo, EstacionamientoCasilla, Casilla

# Register your models here.

class CasillaAtributos(admin.ModelAdmin):
    list_display = ["id", "posicion"]

class EstacionamientoAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre_usuario_dueno", "direccion", "tarifahora", "disponible"]
    search_fields = ["direccion", "id_dueno__nombreusuario"]
    list_filter = ["disponible", "direccion"]

    def nombre_usuario_dueno(self, obj):
        return obj.id_dueno.nombreusuario if obj.id_dueno else ''
    nombre_usuario_dueno.short_description = 'Nombre de Usuario del Dueño'

admin.site.register(DuenoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Estacionamiento, EstacionamientoAtributos)
admin.site.register(ClienteVehiculo)
admin.site.register(EstacionamientoCasilla)
admin.site.register(Casilla, CasillaAtributos)