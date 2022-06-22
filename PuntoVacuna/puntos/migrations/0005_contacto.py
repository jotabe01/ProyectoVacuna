# Generated by Django 4.0.5 on 2022-06-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0004_centro_comuna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contac', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('correo', models.CharField(max_length=50, null=True)),
                ('comentario', models.CharField(max_length=300)),
                ('asunto', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]