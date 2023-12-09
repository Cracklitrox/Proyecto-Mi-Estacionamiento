from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return 'Nombre de la marca: ' + str(self.nombre)

class Vehiculo(models.Model):
    # id_usuario = models
    patente = models.CharField(max_length=6)
    id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_marca', default=None)
    modelo = models.CharField(max_length=255)
    estacionado = models.BooleanField(default=False, verbose_name='Vehiculo Estacionado')

    def __str__(self):
        return 'ID del vehiculo: ' + str(self.id)

class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=255)
    disponible = models.BooleanField(default=False, verbose_name='Estado Estacionamiento')
    tarifahora = models.IntegerField(db_column='tarifaHora', verbose_name='Tarifa por Hora')
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='fotoEstacionamiento/', null=True, blank=True, verbose_name='Imagen del Estacionamiento')
    id_puntoInteres = models.ForeignKey('geolocalizacion.Puntointeres', models.DO_NOTHING, db_column='id_puntointeres', verbose_name='Punto de Interes')

    def cambiar_estado(self):
        """
        Cambia el estado del estacionamiento (disponible/deshabilitado).
        """
        self.disponible = not self.disponible
        self.save()


# class Casilla(models.Model):
#     id = models.AutoField(primary_key=True)
#     id_estacionamiento = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='id_estacionamiento')
#     casilla = models.CharField(max_length=30)
#     disponible = models.BooleanField(default=True)

#     def __str__(self):
#         return 'ID Casilla: ' + str(self.id) 

class Casilla(models.Model):
    id = models.AutoField(primary_key=True)
    id_estacionamiento = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='id_estacionamiento', default=None)
    casilla = models.CharField(max_length=30)
    disponible = models.BooleanField(default=True)

    def cambiar_casilla(self):
        """
        Cambia el estado del estacionamiento (disponible/deshabilitado).
        """
        self.disponible = not self.disponible
        self.save()

    def __str__(self):
        return 'ID Casilla: ' + str(self.id) 