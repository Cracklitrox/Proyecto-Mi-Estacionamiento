from django.contrib import admin
from .models import Vehiculo, DuenoVehiculo, Estacionamiento, ClienteVehiculo

# Register your models here.

admin.site.register(DuenoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Estacionamiento)
admin.site.register(ClienteVehiculo)