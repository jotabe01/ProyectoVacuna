from django.contrib import admin
from django.urls import path, include
from .views import home, inicio, lista_usuarios, registrar_usuario,registro, eliminar_usuario
urlpatterns = [
    path('', home, name="home" ),
    path('inicio', inicio, name="inicio" ),
    path('lista_usuarios', lista_usuarios, name="lista_usuarios" ),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario" ),
    path('registro', registro, name="registro" ),
    path('eliminar_usuario/<id>', eliminar_usuario, name="eliminar_usuario" ),
]
