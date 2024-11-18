# Generated by Django 5.1.3 on 2024-11-18 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0003_alter_servicio_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='duracion',
            field=models.CharField(help_text='En minutos', max_length=2),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
