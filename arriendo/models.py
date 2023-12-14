from django.db import models
from estacionamiento.models import Estacionamiento
# Usuario
from usuario.models import ClienteProfile

# Create your models here.

class Arriendo(models.Model):
    id_cliente = models.ForeignKey(ClienteProfile,  on_delete=models.CASCADE, null=True)
    id_estacionamiento = models.ForeignKey('estacionamiento.Estacionamiento', on_delete=models.CASCADE, db_column='id_estacionamiento', verbose_name='Estacionamiento')
    horainicio = models.DateTimeField(db_column='horaInicio', verbose_name='Hora de Inicio')
    horafin = models.DateTimeField(db_column='horaFin', verbose_name='Hora de Fin')
    preciototal = models.IntegerField(db_column='precioTotal', verbose_name='Precio Total')
    
    calificacioncliente = models.DecimalField(db_column='calificacionCliente', max_digits=2, decimal_places=1, blank=True, null=True, verbose_name='Calificacion para el Cliente')
    calificaciondueno = models.DecimalField(db_column='calificacionDueno', max_digits=2, decimal_places=1, blank=True, null=True, verbose_name='Calificacion para el Dueño')

    def __str__(self):
        return ' Arriendo numero: ' + str(self.id)