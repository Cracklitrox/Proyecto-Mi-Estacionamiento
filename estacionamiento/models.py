from django.db import models
from dueno.models import Dueno
from cliente.models import Cliente

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
    coordenadasgps = models.CharField(db_column='coordenadasGPS', max_length=255, verbose_name='Coordenadas GPS')
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'ID y Dueño del Estacionamiento: ' + str(self.id) + ' / ' + str(self.id_dueno)

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