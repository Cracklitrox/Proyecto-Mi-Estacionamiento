from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from usuario.models import Usuario

class Cliente(Usuario):
    imagen_cliente = models.ImageField(_('Imagen'),upload_to='imagenCliente/', null=True, blank=True)
    calificacion_promedio_cliente = models.DecimalField(_('Calificacion Promedio del Cliente'),max_digits=2, decimal_places=1, null=True, blank=True)
    groups = models.ManyToManyField(Group)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        grupo_cliente, created = Group.objects.get_or_create(name='Cliente')
        self.groups.add(grupo_cliente)