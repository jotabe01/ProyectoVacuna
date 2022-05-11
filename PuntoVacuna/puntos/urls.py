from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, inicio, lista_usuarios, registrar_usuario,registro, eliminar_usuario, form_login, login_view, logout_view

urlpatterns = [
    path('', home, name="home" ),
    path('inicio', inicio, name="inicio" ),
    path('lista_usuarios', lista_usuarios, name="lista_usuarios" ),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario" ),
    path('registro', registro, name="registro" ),
    path('eliminar_usuario/<id>', eliminar_usuario, name="eliminar_usuario" ),

    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
]
