# Generated by Django 4.0.5 on 2022-06-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0002_vacuna_descripcion_vacuna_lab'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
