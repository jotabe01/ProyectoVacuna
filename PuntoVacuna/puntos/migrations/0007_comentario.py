# Generated by Django 4.0.5 on 2022-06-22 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0006_centro_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_contac', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=300, null=True)),
                ('like', models.IntegerField(null=True)),
                ('dislike', models.IntegerField(null=True)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puntos.centro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puntos.usuario')),
            ],
        ),
    ]
