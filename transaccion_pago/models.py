from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from usuario.models import User

# Create your models here.

class Banco(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='fotoBanco/', null=True, blank=True, verbose_name='Imagen del Banco')
    def __str__(self):
        return 'Nombre del Banco: ' + self.nombre

class Tarjetacredito(models.Model):
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE, null=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_titular = models.CharField(max_length=20, default=None)
    numero = models.CharField(max_length=16, verbose_name='Numero de la Tarjeta')
    fechavencimiento = models.DateField(db_column='fechaVencimiento', verbose_name='Fecha de Vencimiento')
    cvv = models.IntegerField(db_column='CVV')

    def __str__(self):
        return 'ID de la Tarjeta: ' + str(self.id) + ' / Numero de la Tarjeta: ' + str(self.numero)