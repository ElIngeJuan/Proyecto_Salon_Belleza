# Generated by Django 5.1.3 on 2024-11-18 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0001_initial'),
        ('Servicio', '0002_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicio.servicio'),
        ),
    ]
