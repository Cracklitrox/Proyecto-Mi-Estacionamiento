from django.contrib import admin
from .models import Vehiculo, DuenoVehiculo, Estacionamiento, ClienteVehiculo, EstacionamientoCasilla, Casilla

# Register your models here.

admin.site.register(DuenoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(Estacionamiento)
admin.site.register(ClienteVehiculo)
admin.site.register(EstacionamientoCasilla)
admin.site.register(Casilla)