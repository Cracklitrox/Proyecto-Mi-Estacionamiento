from django.db import models

# Create your models here.

class Puntointeres(models.Model):
    id = models.AutoField(primary_key=True)
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} (Latitud: {self.latitud} - Longitud: {self.longitud})"