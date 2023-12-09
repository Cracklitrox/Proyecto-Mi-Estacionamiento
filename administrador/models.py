from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Administrador(AbstractUser):
    first_name = models.CharField(_('Nombre'), max_length=30, blank=True)
    last_name = models.CharField(_('Apellido'), max_length=150, blank=True)
    telefono = models.IntegerField()
    foto_perfil = models.ImageField(upload_to='fotoAdministrador/', null=True, blank=True)
    email = models.EmailField(_('Correo Electronico'), blank=True)
    username = models.CharField(_('Nombre de Administrador'), max_length=150, unique=True)
    password = models.CharField(_('Contraseña'), max_length=128)
    is_staff = models.BooleanField(_('Es Administrador?'), default=True)
    is_superuser = models.BooleanField(_('Es Super Usuario?'), default=True)
    is_active = models.BooleanField(_('Activo'), default=True)
    last_login = models.DateTimeField(_('Ultima Sesion'), blank=True, null=True)
    date_joined = models.DateTimeField(_('Fecha de Creacion'), auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('grupos'),
        blank=True,
        help_text=_('Los grupos a los que pertenece este administrador.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('permisos de administrador'),
        blank=True,
        help_text=_('Permisos específicos para este administrador.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    pass