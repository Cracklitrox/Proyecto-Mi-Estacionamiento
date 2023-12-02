from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from django.db.models import Count
from .models import Region, Provincia, Comuna

# Register your models here.

class ComunaAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre", "provincia"]
    search_fields = ["nombre", "id_provincia__nombre"]
    list_filter = ["nombre", ("id_provincia", admin.RelatedOnlyFieldListFilter)]

    def provincia(self, obj):
        return obj.id_provincia.nombre if obj.id_provincia else ''
    provincia.short_description = 'Pertenece a la provincia de'


class ProvinciaAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre", "region", "link_cantidad_comunas"]
    search_fields = ["nombre", "id_region__nombre"]
    list_filter = ["nombre", ("id_region", admin.RelatedOnlyFieldListFilter)]

    def region(self, obj):
        return obj.id_region.nombre if obj.id_region else ''
    region.short_description = 'Pertenece a la región de'

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(cantidad_comunas=Count('comuna'))
        return queryset

    def link_cantidad_comunas(self, obj):
        url = reverse('admin:usuario_comuna_changelist') + f'?id_provincia__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, obj.cantidad_comunas)
    link_cantidad_comunas.short_description = 'Cantidad de Comunas'

class RegionAtributos(admin.ModelAdmin):
    list_display = ["id", "nombre", "link_cantidad_provincias"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(cantidad_provincias=Count('provincia'))
        return queryset
    
    def link_cantidad_provincias(self, obj):
        url = reverse('admin:usuario_provincia_changelist') + f'?id_region__id__exact={obj.id}'
        return format_html('<a href="{}">{}</a>', url, obj.cantidad_provincias)
    link_cantidad_provincias.short_description = 'Cantidad de Provincias'

admin.site.register(Region, RegionAtributos)
admin.site.register(Provincia, ProvinciaAtributos)
admin.site.register(Comuna, ComunaAtributos)