from django.db import models
from django.contrib.auth.hashers import make_password
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna

# Create your models here.

class Dueno(models.Model):
    id = models.AutoField(primary_key=True)
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30, verbose_name='Primer Nombre')
    snombre = models.CharField(max_length=30, verbose_name='Segundo Nombre')
    appaterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    correoelectronico = models.CharField(db_column='correoElectronico', max_length=65, verbose_name='Correo Electronico')
    telefono = models.IntegerField(verbose_name='Telefono')
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20, verbose_name='Nombre de Usuario')
    contrasena = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    calificacionpromedio = models.DecimalField(db_column='calificacionPromedio', max_digits=2, decimal_places=1, verbose_name='Calificacion Promedio', blank=True, null=True)
    escliente = models.BooleanField(default=False, db_column='esCliente', verbose_name='Activar modo Cliente')
    activo = models.BooleanField(default=True, verbose_name='Dueño Activo')
    imagen = models.ImageField(upload_to='fotoDueno/', null=True, blank=True, verbose_name='Imagen del Dueño')
    id_tarjetacredito = models.ForeignKey('transaccion_pago.Tarjetacredito', models.DO_NOTHING, db_column='id_tarjetaCredito', verbose_name='Tarjeta de Credito')
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco', verbose_name='Banco')
    id_comuna = models.ForeignKey('usuario.Comuna', models.DO_NOTHING, db_column='id_comuna', verbose_name='Comuna')

    def save(self, *args, **kwargs):
        if not self.id or self.contrasena != Dueno.objects.get(id=self.id).contrasena:
            self.contrasena = make_password(self.contrasena);
        super (Dueno, self).save(*args, **kwargs)

    def __str__(self):    
        return self.nombreusuario + ' / Estado: ' + str(self.activo)

    class Meta:
        managed = False
        db_table = 'dueno'
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'

class Puntointeres(models.Model):
    id = models.AutoField(primary_key=True)
    latitud = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} (Latitud: {self.latitud} - Longitud: {self.longitud})"

    class Meta:
        managed = False
        db_table = 'puntointeres'
        verbose_name = "Punto de Interes"
        verbose_name_plural = "Punto de Intereses"