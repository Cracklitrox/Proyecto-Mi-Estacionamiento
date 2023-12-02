from django.contrib import admin
from .models import Administrador

# Register your models here.

class AdministradorAtributos(admin.ModelAdmin):
    list_display = ["nombreusuario", "correoelectronico", "telefono", "nivelpermiso", "estadoempleo"]
    search_fields = ["nombreusuario"]
    list_filter = ["nivelpermiso", "estadoempleo"]

admin.site.register(Administrador, AdministradorAtributos)