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

    class Meta:
        managed = False
        db_table = 'vehiculo'
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

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

    class Meta:
        managed = False
        db_table = 'estacionamiento'
        verbose_name = 'Estacionamiento'
        verbose_name_plural = 'Estacionamientos'

class DuenoVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno', verbose_name='Dueño')
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', verbose_name='Vehiculo')

    def __str__(self):
        return 'Dueño: ' + str(self.id) + ' / ' + str(self.id_vehiculo)

    class Meta:
        managed = False
        db_table = 'dueno_vehiculo'
        verbose_name = 'Vehiculo/Dueño'
        verbose_name_plural = 'Vehiculos/Dueño'

class ClienteVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', verbose_name='Cliente')
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', verbose_name='Vehiculo')

    def __str__(self):
        return 'Cliente: ' + str(self.id) + ' / ' + str(self.id_vehiculo)

    class Meta:
        managed = False
        db_table = 'cliente_vehiculo'
        verbose_name = 'Vehiculo/Cliente'
        verbose_name_plural = 'Vehiculos/Cliente'

class Casilla(models.Model):
    id = models.AutoField(primary_key=True)
    posicion = models.CharField(max_length=30)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='fotoCasilla/', null=True, blank=True, verbose_name='Imagen de la Casilla del Estacionamiento')

    def __str__(self):
        return 'ID Casilla: ' + str(self.id) + ' / Estado: ' + str(self.disponible)

    class Meta:
        managed = False
        db_table = 'casilla'
        verbose_name = 'Casilla'
        verbose_name_plural = 'Casillas'

class EstacionamientoCasilla(models.Model):
    id = models.AutoField(primary_key=True)
    id_estacionamiento = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='id_estacionamiento')
    id_casilla = models.ForeignKey(Casilla, models.DO_NOTHING, db_column='id_casilla')

    def __str__(self):
        return 'ID Estacionamiento: {} / ID Casilla: {}'.format(self.id_estacionamiento.id, self.id_casilla.id)

    class Meta:
        managed = False
        db_table = 'estacionamiento_casilla'
        verbose_name = 'Estacionamiento/Casilla'
        verbose_name_plural = 'Estacionamientos/Casillas'