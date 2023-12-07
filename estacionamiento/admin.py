from django.contrib import admin
from .models import Vehiculo, Estacionamiento, Casilla, Marca

# Register your models here.

class CasillaAtributos(admin.ModelAdmin):
    list_display = ["id", "disponible"]

# class EstacionamientoAtributos(admin.ModelAdmin):
#     list_display = ["id", "nombre_usuario_dueno", "direccion", "tarifahora", "disponible"]
#     search_fields = ["direccion", "id_dueno__nombreusuario"]
#     list_filter = ["disponible", "direccion"]

#     def nombre_usuario_dueno(self, obj):
#         return obj.id_dueno.nombreusuario if obj.id_dueno else ''
#     nombre_usuario_dueno.short_description = 'Nombre de Usuario del Dueño'

admin.site.register(Vehiculo)
admin.site.register(Estacionamiento)
admin.site.register(Casilla, CasillaAtributos)
admin.site.register(Marca)