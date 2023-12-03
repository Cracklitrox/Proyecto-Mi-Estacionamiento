from django.db import models

# Create your models here.

class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='fotoBanco/', null=True, blank=True, verbose_name='Imagen del Banco')
    def __str__(self):
        return 'Nombre del Banco: ' + self.nombre
    
    class Meta:
        managed = False
        db_table = 'banco'
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

class Tarjetacredito(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=16, verbose_name='Numero de la Tarjeta')
    fechavencimiento = models.DateField(db_column='fechaVencimiento', verbose_name='Fecha de Vencimiento')
    cvv = models.IntegerField(db_column='CVV')

    def __str__(self):
        return 'ID de la Tarjeta: ' + str(self.id) + ' / Numero de la Tarjeta: ' + str(self.numero)

    class Meta:
        managed = False
        db_table = 'tarjetacredito'
        verbose_name = 'Tarjeta de Credito'
        verbose_name_plural = 'Tarjetas de Credito'