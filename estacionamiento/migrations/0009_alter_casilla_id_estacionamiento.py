# Generated by Django 4.2.7 on 2023-12-12 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamiento', '0008_remove_estacionamiento_id_casillas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casilla',
            name='id_estacionamiento',
            field=models.ForeignKey(db_column='id_estacionamiento', null=True, on_delete=django.db.models.deletion.CASCADE, to='estacionamiento.estacionamiento', verbose_name='Estacionamientos'),
        ),
    ]