# Generated by Django 4.2.7 on 2023-12-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puntointeres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitud', models.CharField(max_length=255)),
                ('longitud', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
    ]
