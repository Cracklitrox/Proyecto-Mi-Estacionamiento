from django.contrib import admin
from .models import Banco, Tarjetacredito
# Register your models here.

class BancoAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

class TarjetacreditoAtributos(admin.ModelAdmin):
    list_display = ["id", "numero", "fechavencimiento"]
    search_fields = ["numero"]
    list_filter = ["numero"]

admin.site.register(Banco, BancoAtributos)
admin.site.register(Tarjetacredito, TarjetacreditoAtributos)