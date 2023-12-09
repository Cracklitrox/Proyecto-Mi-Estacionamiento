from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Group
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
        if extra_fields.get('is_cliente'):
            ClienteProfile.objects.create(user=user)
            grupo_cliente, _ = Group.objects.get_or_create(name='Cliente')
            user.groups.add(grupo_cliente)
        elif extra_fields.get('is_dueno'):
            DuenoProfile.objects.create(user=user)
            grupo_dueno, _ = Group.objects.get_or_create(name='Dueno')
            user.groups.add(grupo_dueno)
        elif extra_fields.get('is_staff'):
            AdminProfile.objects.create(user=user)

        return user
    
    def create_cliente(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_cliente', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_dueno(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_dueno', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_admin(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class ClienteProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    vehiculos = models.IntegerField()
    tarjetas = models.IntegerField()
    telefono = models.IntegerField('Teléfono', null=True)

class DuenoProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    estacionamiento = models.IntegerField(default=0)
    telefono = models.IntegerField('Teléfono', null=True)

class AdminProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    permisos = models.IntegerField(default=0)  # O cualquier otro valor predeterminado que desees

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    usuario_activo = models.BooleanField(default=True)
    pnombre = models.CharField('Primer nombre', max_length=30, blank=True)
    snombre = models.CharField('Segundo nombre', max_length=30, blank=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    is_cliente = models.BooleanField(default=False)
    is_dueno = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'pnombre', 'snombre', 'apellidos']

    objects = UserManager()

    def get_full_name(self):
        full_name = self.pnombre
        if self.snombre:
            full_name += ' ' + self.snombre
        if self.apellidos:
            full_name += ' ' + self.apellidos
        return full_name

    def get_short_name(self):
        return self.pnombre

    def get_profile(self):
        if self.is_cliente:
            return getattr(self, 'cliente_profile', None)
        elif self.is_dueno:
            return getattr(self, 'dueno_profile', None)
        else:
            return None