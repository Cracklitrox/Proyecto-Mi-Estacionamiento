# Generated by Django 4.2.7 on 2023-12-09 07:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.usuario')),
                ('estacionamientos', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Estacionamientos')),
                ('imagen_dueno', models.ImageField(blank=True, null=True, upload_to='imagenDueno/', verbose_name='Imagen')),
                ('calificacion_promedio_dueno', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Calificacion Promedio del Dueño')),
                ('groups', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'abstract': False,
            },
            bases=('usuario.usuario',),
        ),
    ]
