from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey("Region", models.DO_NOTHING, db_column="id_region", verbose_name='Region')

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_provincia = models.ForeignKey("Provincia", models.DO_NOTHING, db_column="id_provincia", verbose_name='Provincia')

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    nombre = models.CharField(max_length=25)
    appaterno = models.CharField(max_length=30)
    apmaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()
    vehiculos = models.IntegerField(null=True, blank=True)
    tarjetas_credito = models.IntegerField()
    estacionamientos = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to='usuarioImagen/', null=True, blank=True)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calificacion_promedio_dueno = models.DecimalField(max_digits=3, decimal_places=2, null=True,  blank=True, default=None)
    calificacion_promedio_cliente = models.DecimalField(max_digits=3, decimal_places=2, null=True,  blank=True, default=None)
    es_dueno = models.BooleanField(default=False)
    es_cliente = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} - {self.nombre} {self.appaterno} {self.apmaterno}'