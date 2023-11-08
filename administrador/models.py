from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from usuario.models import Region

# Create your models here.

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30, verbose_name='Primer Nombre')
    snombre = models.CharField(max_length=30, verbose_name='Segundo Nombre')
    appaterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    correoelectronico = models.CharField(db_column='correoElectronico', max_length=65, verbose_name='Correo Electronico')
    telefono = models.IntegerField(verbose_name= 'Telefono')
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20, verbose_name='Nombre de Usuario')
    contrasena = models.CharField(max_length=30, verbose_name='Contraseña')
    fechacontratacion = models.DateField(db_column='fechaContratacion', verbose_name='Fecha Contratacion')
    nivelpermiso = models.IntegerField(db_column='nivelPermiso', verbose_name='Nivel de Permiso')
    estadoempleo = models.BooleanField(db_column='estadoEmpleo', default=True, verbose_name='Estado de empleo')
    ultimoacceso = models.DateTimeField(db_column='ultimoAcceso', verbose_name='Ultimo Acceso')
    id_region = models.ForeignKey('usuario.Region', models.DO_NOTHING, db_column='id_region', verbose_name='Región')

    def __str__(self):
        return self.nombreusuario + ' / Estado: ' + str(self.estadoempleo)
    class Meta:
        managed = False
        db_table = 'administrador'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'