# Generated by Django 4.0.5 on 2022-06-15 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0003_centro_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='comuna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='puntos.comuna'),
            preserve_default=False,
        ),
    ]
