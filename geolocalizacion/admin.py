from django.contrib import admin
from .models import Puntointeres

# Register your models here.

class PuntointeresAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre", "latitud", "longitud"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

admin.site.register(Puntointeres, PuntointeresAtributos)