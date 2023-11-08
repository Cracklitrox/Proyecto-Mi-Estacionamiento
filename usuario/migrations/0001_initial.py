# Generated by Django 4.2.7 on 2023-11-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Región',
                'verbose_name_plural': 'Regiones',
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
