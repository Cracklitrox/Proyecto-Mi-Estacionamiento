from django.db import models
from dueno.models import Dueno
from cliente.models import Cliente
from geolocalizacion.models import Puntointeres

# Create your models here.

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    estacionado = models.BooleanField(default=False, verbose_name='Vehiculo Estacionado')

    def __str__(self):
        return 'ID del vehiculo: ' + str(self.id)

class Estacionamiento(models.Model):
    id = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno', verbose_name='Dueño')
    direccion = models.CharField(max_length=255)
    disponible = models.BooleanField(default=False, verbose_name='Estado Estacionamiento')
    tarifahora = models.IntegerField(db_column='tarifaHora', verbose_name='Tarifa por Hora')
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='fotoEstacionamiento/', null=True, blank=True, verbose_name='Imagen del Estacionamiento')
    id_puntoInteres = models.ForeignKey('geolocalizacion.Puntointeres', models.DO_NOTHING, db_column='id_puntointeres', verbose_name='Punto de Interes')

    def __str__(self):
        return 'ID: ' + str(self.id) + ' / Dueño del Estacionamiento: ' + str(self.id_dueno.nombreusuario)

    def cambiar_estado(self):
        """
        Cambia el estado del estacionamiento (disponible/deshabilitado).
        """
        self.disponible = not self.disponible
        self.save()
class DuenoVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno', verbose_name='Dueño')
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', verbose_name='Vehiculo')

    def __str__(self):
        return 'Dueño: ' + str(self.id) + ' / ' + str(self.id_vehiculo)

class ClienteVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', verbose_name='Cliente')
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', verbose_name='Vehiculo')

    def __str__(self):
        return 'Cliente: ' + str(self.id) + ' / ' + str(self.id_vehiculo)

class Casilla(models.Model):
    id = models.AutoField(primary_key=True)
    posicion = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='fotoCasilla/', null=True, blank=True, verbose_name='Imagen de la Casilla del Estacionamiento')

    

    def __str__(self):
        return 'ID Casilla: ' + str(self.id) 

class EstacionamientoCasilla(models.Model):
    id = models.AutoField(primary_key=True)
    id_estacionamiento = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='id_estacionamiento')
    id_casilla = models.ForeignKey(Casilla, models.DO_NOTHING, db_column='id_casilla')
    disponible = models.BooleanField(default=True)

    def cambiar_casilla(self):
        """
        Cambia el estado del estacionamiento (disponible/deshabilitado).
        """
        self.disponible = not self.disponible
        self.save()

    def __str__(self):
        return 'ID Estacionamiento: {} / ID Casilla: {}'.format(self.id_estacionamiento.id, self.id_casilla.id) + ' / Estado: ' + str(self.disponible)
