from django.db import models
from cliente.models import Cliente
from dueno.models import Dueno
from estacionamiento.models import Estacionamiento

# Create your models here.

class Arriendo(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('cliente.Cliente', models.DO_NOTHING, db_column='id_cliente', verbose_name='Cliente')
    id_dueno = models.ForeignKey('dueno.Dueno', models.DO_NOTHING, db_column='id_dueno', verbose_name='Dueño')
    id_estacionamiento = models.ForeignKey('estacionamiento.Estacionamiento', models.DO_NOTHING, db_column='id_estacionamiento', verbose_name='Estacionamiento')
    horainicio = models.DateTimeField(db_column='horaInicio', verbose_name='Hora de Inicio')
    horafin = models.DateTimeField(db_column='horaFin', verbose_name='Hora de Fin')
    preciototal = models.IntegerField(db_column='precioTotal', verbose_name='Precio Total')
    calificacioncliente = models.DecimalField(db_column='calificacionCliente', max_digits=2, decimal_places=1, blank=True, null=True, verbose_name='Calificacion para el Cliente')
    calificaciondueno = models.DecimalField(db_column='calificacionDueno', max_digits=2, decimal_places=1, blank=True, null=True, verbose_name='Calificacion para el Dueño')

    def __str__(self):
        return ' Arriendo numero: ' + str(self.id)