# Generated by Django 4.2.7 on 2023-11-07 18:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(8)])),
                ('dv_run', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(max_length=30)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('correoelectronico', models.CharField(db_column='correoElectronico', max_length=65)),
                ('telefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9)])),
                ('nombreusuario', models.CharField(db_column='nombreUsuario', max_length=20)),
                ('contrasena', models.CharField(max_length=30)),
                ('fechacontratacion', models.DateField(db_column='fechaContratacion')),
                ('nivelpermiso', models.IntegerField(db_column='nivelPermiso')),
                ('estadoempleo', models.BooleanField(db_column='estadoEmpleo', default=True)),
                ('ultimoacceso', models.DateTimeField(db_column='ultimoAcceso')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'db_table': 'administrador',
                'managed': False,
            },
        ),
    ]
