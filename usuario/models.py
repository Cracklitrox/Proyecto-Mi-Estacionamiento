from django.db import models

# Create your models here.


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = "region"
        verbose_name = "Región"
        verbose_name_plural = "Regiones"


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey("Region", models.DO_NOTHING, db_column="id_region", verbose_name='Region')

    def __str__(self):
        return f"{self.nombre} - {self.id_region.nombre}"

    class Meta:
        managed = False
        db_table = "provincia"
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_provincia = models.ForeignKey("Provincia", models.DO_NOTHING, db_column="id_provincia", verbose_name='Provincia')

    def __str__(self):
        provincia_nombre = self.id_provincia.nombre if self.id_provincia else "Sin provincia"

        region_nombre = self.id_provincia.id_region.nombre if (self.id_provincia and self.id_provincia.id_region) else "Sin región"

        return f"{self.nombre} - {provincia_nombre} - {region_nombre}"

    class Meta:
        managed = False
        db_table = "comuna"
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"