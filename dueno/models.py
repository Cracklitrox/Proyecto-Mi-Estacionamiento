from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from usuario.models import Usuario

class Dueno(Usuario):
    estacionamientos = models.IntegerField(_('Cantidad de Estacionamientos'), null=True, blank=True, validators=[MinValueValidator(0)])
    imagen_dueno = models.ImageField(_('Imagen'),upload_to='imagenDueno/', null=True, blank=True)
    calificacion_promedio_dueno = models.DecimalField(_('Calificacion Promedio del Dueño'),max_digits=2, decimal_places=1, null=True, blank=True)
    groups = models.ManyToManyField(Group)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        grupo_dueno, created = Group.objects.get_or_create(name='Dueno')
        self.groups.add(grupo_dueno)