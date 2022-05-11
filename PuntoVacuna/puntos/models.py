from django.db import models
from django.contrib.auth.models import User

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
# Create your models here.
class Usuario(models.Model):
    num_run = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50,null=True)
    appellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=30,null=True)
    clave = models.CharField(max_length=128,null=True)
    nombre_usr = models.CharField(max_length=20,null=True)
    

    user =  models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres


class Vacuna(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.nombre


class Centro(models.Model):
    id_centro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=True)
    descripcion = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.nombre

class DireccionU(models.Model):
    id_direccionu = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
   
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_direccion

class DireccionC(models.Model):
    id_direccionc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
  

    centro = models.ForeignKey(Centro,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_direccion

