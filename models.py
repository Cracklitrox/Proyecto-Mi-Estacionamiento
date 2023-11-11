# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    correoelectronico = models.CharField(db_column='correoElectronico', max_length=65)  # Field name made lowercase.
    telefono = models.IntegerField()
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20)  # Field name made lowercase.
    contrasena = models.CharField(max_length=30)
    fechacontratacion = models.DateField(db_column='fechaContratacion')  # Field name made lowercase.
    nivelpermiso = models.IntegerField(db_column='nivelPermiso')  # Field name made lowercase.
    estadoempleo = models.IntegerField(db_column='estadoEmpleo')  # Field name made lowercase.
    ultimoacceso = models.DateTimeField(db_column='ultimoAcceso')  # Field name made lowercase.
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Arriendo(models.Model):
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_dueno = models.ForeignKey('Dueno', models.DO_NOTHING, db_column='id_dueno', blank=True, null=True)
    id_estacionamiento = models.ForeignKey('Estacionamiento', models.DO_NOTHING, db_column='id_estacionamiento', blank=True, null=True)
    horainicio = models.DateTimeField(db_column='horaInicio')  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='horaFin')  # Field name made lowercase.
    preciototal = models.IntegerField(db_column='precioTotal')  # Field name made lowercase.
    calificacioncliente = models.DecimalField(db_column='calificacionCliente', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    calificaciondueno = models.DecimalField(db_column='calificacionDueno', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'arriendo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'banco'


class Casilla(models.Model):
    posicion = models.CharField(max_length=30)
    disponible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casilla'


class Cliente(models.Model):
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    correoelectronico = models.CharField(db_column='correoElectronico', max_length=65)  # Field name made lowercase.
    telefono = models.IntegerField()
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20)  # Field name made lowercase.
    contrasena = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    calificacionpromedio = models.DecimalField(db_column='calificacionPromedio', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField()
    id_tarjetacredito = models.ForeignKey('Tarjetacredito', models.DO_NOTHING, db_column='id_tarjetaCredito', blank=True, null=True)  # Field name made lowercase.
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteVehiculo(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_vehiculo'


class Comuna(models.Model):
    nombre = models.CharField(max_length=255)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dueno(models.Model):
    run = models.IntegerField()
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    correoelectronico = models.CharField(db_column='correoElectronico', max_length=65)  # Field name made lowercase.
    telefono = models.IntegerField()
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20)  # Field name made lowercase.
    contrasena = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    calificacionpromedio = models.DecimalField(db_column='calificacionPromedio', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    escliente = models.IntegerField(db_column='esCliente')  # Field name made lowercase.
    activo = models.IntegerField()
    id_tarjetacredito = models.ForeignKey('Tarjetacredito', models.DO_NOTHING, db_column='id_tarjetaCredito', blank=True, null=True)  # Field name made lowercase.
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dueno'


class DuenoVehiculo(models.Model):
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno', blank=True, null=True)
    id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dueno_vehiculo'


class Estacionamiento(models.Model):
    id_dueno = models.ForeignKey(Dueno, models.DO_NOTHING, db_column='id_dueno', blank=True, null=True)
    direccion = models.CharField(max_length=255)
    disponible = models.IntegerField()
    tarifahora = models.IntegerField(db_column='tarifaHora')  # Field name made lowercase.
    coordenadasgps = models.CharField(db_column='coordenadasGPS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacionamiento'


class EstacionamientoCasilla(models.Model):
    id_estacionamiento = models.ForeignKey(Estacionamiento, models.DO_NOTHING, db_column='id_estacionamiento', blank=True, null=True)
    id_casilla = models.ForeignKey(Casilla, models.DO_NOTHING, db_column='id_casilla', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacionamiento_casilla'


class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'


class Tarjetacredito(models.Model):
    numero = models.CharField(max_length=19)
    fechavencimiento = models.DateField(db_column='fechaVencimiento')  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarjetacredito'


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    estacionado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculo'
