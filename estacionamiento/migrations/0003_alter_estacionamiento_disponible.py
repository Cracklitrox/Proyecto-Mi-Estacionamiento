# Generated by Django 4.2.7 on 2023-12-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='disponible',
            field=models.BooleanField(default=True, verbose_name='Estado Estacionamiento'),
        ),
    ]
