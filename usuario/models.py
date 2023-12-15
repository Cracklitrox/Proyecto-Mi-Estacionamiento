from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Group
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.conf import settings

class Region(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey("Region", models.DO_NOTHING, db_column="id_region", verbose_name='Region')

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
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

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Crear el perfil según el tipo de usuario
        if extra_fields.get('es_cliente'):
            ClienteProfile.objects.create(user=user)
            grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)
        elif extra_fields.get('es_dueno'):
            DuenoProfile.objects.create(user=user)
            grupo_dueno, _ = Group.objects.get_or_create(name='Dueno')
            user.groups.add(grupo_dueno)
        elif extra_fields.get('is_staff'):
            AdministradorProfile.objects.create(user=user)

        return user
    
    def create_cliente(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('es_cliente', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_dueno(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('es_dueno', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_admin(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class UsuarioProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    run = models.IntegerField(_('Run'), validators=[MinValueValidator(1000000), MaxValueValidator(99999999)])
    dv_run = models.CharField(_('Digito Verificador'), max_length=1, validators=[RegexValidator(r'^[1-9K]$')])
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class ClienteProfile(UsuarioProfile):
    calificacion_promedio_cliente = models.DecimalField(_('Calificacion Promedio del Cliente'), default=0, max_digits=2, decimal_places=1, null=True, blank=True)

class DuenoProfile(UsuarioProfile):
    calificacion_promedio_dueno = models.DecimalField(_('Calificacion Promedio del Dueño'), default=0, max_digits=2, decimal_places=1, null=True, blank=True)

class AdministradorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    permisos = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])

class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(_('Nombre'), max_length=30)
    last_name = models.CharField(_('Apellido Paterno'), max_length=30)
    apmaterno = models.CharField(_('Apellido Materno'), max_length=30)
    telefono = models.CharField(_('Teléfono'), max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    es_cliente = models.BooleanField(_('Es cliente'), default=False)
    es_dueno = models.BooleanField(_('Es dueño'), default=False)

    objects = UserManager()

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        if self.apmaterno:
            full_name += f' {self.apmaterno}'
        return full_name

    def get_short_name(self):
        return self.first_name

    def get_profile(self):
        if self.es_cliente:
            return getattr(self, 'cliente_profile', None)
        elif self.es_dueno:
            return getattr(self, 'dueno_profile', None)
        else:
            return None