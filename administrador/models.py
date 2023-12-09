from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     # Campos personalizados
#     nombre = models.CharField(max_length=30)
#     apellidos = models.CharField(max_length=30)
#     nivel_permiso = models.IntegerField(default=0)
#     imagen = models.ImageField(upload_to='administradorImagen/', blank=True, null=True)

#     # Agregar related_name único para evitar conflictos con los campos groups y user_permissions
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',
#         blank=True,
#         verbose_name='groups',
#         help_text='Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos otorgados a cada uno de sus grupos.',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Permisos específicos para este usuario.',
#     )