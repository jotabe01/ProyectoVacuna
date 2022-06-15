from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import  eliminar_centro, guardar_centro, home,registrar_comuna,guardar_comuna, inicio, lista_centros, lista_usuarios, modificar_centro, registrar_usuario,registro, eliminar_usuario, form_login, login_view, logout_view, registrar2, modificar_usuario, modificar_us, buscar_usuario, registrar,registrar_centro,  lista_centros, eliminar_centro, guardar_centro, modificar_centro, funcionmodcen, buscar_centro, guardar_vacuna, eliminar_vacuna, registrar_vacuna, lista_vacunas, funcionmodvac, modificar_vacuna, buscar_vacuna


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
    #centro
    path('registrar_centro',login_required(registrar_centro), name='registrar_centro'),
    path('lista_centros',login_required(lista_centros), name="lista_centros"),
    path('guardar_centro',guardar_centro, name="guardar_centro"),
    path('eliminar_centro/<id>',eliminar_centro, name="eliminar_centro"),
    
    path('modificar_centro/<id>', modificar_centro,name="modificar_centro"),
    path('funcionmodcen',funcionmodcen,name="funcionmodcen"),
    path('buscar_centro',login_required(buscar_centro),name="buscar_centro"),
    #vacuna
    path('registrar_vacuna',login_required(registrar_vacuna), name='registrar_vacuna'),
    path('guardar_vacuna',guardar_vacuna, name="guardar_vacuna"),
    path('eliminar_vacuna/<id>',eliminar_vacuna, name="eliminar_vacuna"),
    path('lista_vacunas',login_required(lista_vacunas), name="lista_vacunas"),
    path('modificar_vacuna/<id>', modificar_vacuna,name="modificar_vacuna"),
    path('funcionmodvac', funcionmodvac,name="funcionmodvac"),
    path('buscar_vacuna',login_required(buscar_vacuna),name="buscar_vacuna"),
    #comuna
    path('registrar_comuna',login_required(registrar_comuna), name="registrar_comuna"),
    path('guardar_comuna',login_required(guardar_comuna), name="guardar_comuna"),


    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
]
