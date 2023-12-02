from django.contrib import admin
from .models import Dueno

# Register your models here.

class DuenoAtributos(admin.ModelAdmin):
    list_display = ["rut_con_dv", "nombreusuario", "correoelectronico", "telefono", "calificacionpromedio"]
    search_fields = ["run", "dv_run", "nombreusuario"]
    list_filter = ["activo", "calificacionpromedio"]

    def rut_con_dv(self, obj):
        return f"{obj.run}-{obj.dv_run}"
    rut_con_dv.short_description = 'RUT'

admin.site.register(Dueno, DuenoAtributos)