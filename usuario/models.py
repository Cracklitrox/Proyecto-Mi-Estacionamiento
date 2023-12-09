from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
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

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, contrasena=None):
        if not nombre_usuario:
            raise ValueError('El nombre de usuario es obligatorio')

        user = self.model(nombre_usuario=nombre_usuario)
        user.set_password(contrasena)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    run = models.IntegerField(_('Run'), validators=[MinValueValidator(1000000), MaxValueValidator(99999999)])
    dv_run = models.CharField(_('Digito Verificador'), max_length=1, validators=[RegexValidator(r'^[1-9K]$')])
    nombre = models.CharField(_('Nombre'), max_length=30, validators=[RegexValidator(r'^[a-zA-Z]+$')])
    appaterno = models.CharField(_('Apellido Paterno'), max_length=55, validators=[RegexValidator(r'^[a-zA-Z]+$')])
    apmaterno = models.CharField(_('Apellido Materno'), max_length=55, validators=[RegexValidator(r'^[a-zA-Z]+$')])
    nombre_usuario = models.CharField(_('Nombre de Usuario'), max_length=20, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9@]+$')])
    email = models.EmailField(_('Correo Electronico'), unique=True)
    telefono = models.IntegerField(_('Telefono'), unique=True)
    direccion = models.CharField(_('Direccion'), max_length=70)
    vehiculos = models.IntegerField(_('Cantidad de Vehiculos'), null=True, blank=True, validators=[MinValueValidator(0)])
    tarjetas_credito = models.IntegerField(_('Cantidad de Tarjetas de Credito'), null=True, blank=True, validators=[MinValueValidator(0)])
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    USERNAME_FIELD = 'nombre_usuario'

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