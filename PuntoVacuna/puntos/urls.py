from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import  eliminar_centro, guardar_centro, home, inicio, lista_centros, lista_usuarios, mod_centro, modificar_centro, registrar_centro, registrar_usuario,registro, eliminar_usuario, form_login, login_view, logout_view, registrar2, modificar_usuario, modificar_us, buscar_usuario, registrar
registrar_centro,  lista_centros, mod_centro, eliminar_centro, guardar_centro,
urlpatterns = [
    path('', home, name="home" ),
    path('inicio', inicio, name="inicio" ),
    path('lista_usuarios', login_required(lista_usuarios), name="lista_usuarios" ),
    path('registrar_usuario', login_required(registrar_usuario), name="registrar_usuario" ),
    path('registro', registro, name="registro" ),
    path('eliminar_usuario/<id>', eliminar_usuario, name="eliminar_usuario" ),
    path('modificar_usuario/<id>', modificar_usuario, name="modificar_usuario" ),
    path('modificar_us',login_required(modificar_us) ,name="modificar_us"),
    path('buscar_usuario',login_required(buscar_usuario),name="buscar_usuario") ,
    path('registrar',registrar,name="registrar") ,
    path('registrar2', registrar2, name="registrar2" ),
    path('registrar_usuario', login_required(registrar_usuario), name="registrar_usuario" ),
    path('registrar_centro',login_required(registrar_centro), name='registrar_centro'),
    path('lista_centros',login_required(lista_centros), name="lista_centros"),
    path('guardar_centro',guardar_centro, name="guardar_centro"),
    path('eliminar_centro/<id>',eliminar_centro, name="eliminar_centro"),
    
    path('modificar_centro/<id>', mod_centro, name='modificar_centro'),
    path('m_centro', login_required(modificar_centro), name='m_centro'),


    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
]
