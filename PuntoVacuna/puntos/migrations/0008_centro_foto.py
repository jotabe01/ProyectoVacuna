# Generated by Django 4.0.5 on 2022-06-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0007_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='foto',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
