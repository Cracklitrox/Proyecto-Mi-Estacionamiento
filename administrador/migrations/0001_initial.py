# Generated by Django 4.2.7 on 2023-12-09 06:33

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Apellido')),
                ('telefono', models.IntegerField()),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotoAdministrador/')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Correo Electronico')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Nombre de Administrador')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Es Administrador?')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='Es Super Usuario?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Ultima Sesion')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('groups', models.ManyToManyField(blank=True, help_text='Los grupos a los que pertenece este administrador.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='auth.group', verbose_name='grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permisos específicos para este administrador.', related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='auth.permission', verbose_name='permisos de administrador')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
