# Generated by Django 4.2.7 on 2023-12-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotoBanco/', verbose_name='Imagen del Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetacredito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_titular', models.CharField(default=None, max_length=20)),
                ('numero', models.CharField(max_length=16, verbose_name='Numero de la Tarjeta')),
                ('fechavencimiento', models.DateField(db_column='fechaVencimiento', verbose_name='Fecha de Vencimiento')),
                ('cvv', models.IntegerField(db_column='CVV')),
            ],
        ),
    ]
