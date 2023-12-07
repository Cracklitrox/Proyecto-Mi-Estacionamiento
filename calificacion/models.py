from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from usuario.models import Usuario

class Calificacion(models.Model):
    id_usuario_entrega = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        related_name='calificaciones_entregadas',
        db_column='id_usuario_entrega',
        verbose_name='ID del que entrega la calificacion'
    )
    id_usuario_recibe = models.ForeignKey(
        Usuario,
        on_delete=models.DO_NOTHING,
        related_name='calificaciones_recibidas',
        db_column='id_usuario_recibe',
        verbose_name='ID del usuario que recibe la calificacion'
    )
    calificacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return 'Calificacion dada por: ' + str(self.id_usuario_entrega.username) + '. Para el usuario: ' + str(self.id_usuario_recibe.username)