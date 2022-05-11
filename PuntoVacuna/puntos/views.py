from django.shortcuts import render, redirect
from .models import Usuario, Tipo_usuario, Comuna, Centro, Vacuna,DireccionC, DireccionU
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
	return render(request, 'puntos/home.html')

def inicio(request):
	return render(request, 'puntos/inicio.html')
	

def lista_usuarios(request):
	usuario = Usuario.objects.all()
	contexto ={
        "usuario":usuario,
       
    }
	return render(request, 'puntos/lista_usuarios.html',contexto)

def registrar_usuario(request):
	return render(request, 'puntos/registrar_usuario.html')


def registro(request):
    nombre_u = request.POST['Nombre']
    appellidos_u = request.POST['Apellidos_per']
    rut_u = request.POST['Rut']
    correo_u = request.POST['correo']
    username_u = request.POST['username']
    contraseña_u = request.POST['Contraseña']
    contraseña_conf = request.POST['Contraseña1']
    tip_u = request.POST['tipu']
    tip_o = Tipo_usuario.objects.get(id_tipo_usuario = tip_u) #al ser foranea debe ser extraida de la otra tabala
    
    try:
        a= User.objects.get(username=username_u )
        messages.error(request,'Nombre de usuario no disponible')
        return redirect('registrar_usuario')

    except User.DoesNotExist:
        try:
            b=Usuario.objects.get(num_run=rut_u)
            messages.error(request,'El Rut no esta disponible')
            return redirect('registrar_usuario')

        except Usuario.DoesNotExist:

            user1 = User.objects.create_user(username_u, correo_u, contraseña_u)
            user1.first_name = nombre_u
            user1.last_name = appellidos_u
            user1.is_staff = 0
            user1.save() 
            if contraseña_conf == contraseña_u:
                a=Usuario.objects.create(nombres = nombre_u, appellidos = appellidos_u, 
                                    num_run = rut_u, correo = correo_u, nombre_usr = username_u, clave = contraseña_u, tipo_usuario = tip_o, user = user1)
                messages.success(request,'Usuario registrado')
            
                return redirect('lista_usuarios')
            else:
                messages.error(request,'La contraseña no coinside')    
                return redirect('registrar_usuario')


def eliminar_usuario(request, id):
    usu = Usuario.objects.get(user_id = id)
    usu.delete()
    usu1 = User.objects.get(id = id)
    usu1.delete()
    messages.success(request,'**El usuario '+usu.nombre_usr+' a sido eliminado exitosalemte.**')

    return redirect('lista_usuarios')

def login_view(request):
    username_u = request.POST['username']
    password_u = request.POST['password']
    user = authenticate(username = username_u, password = password_u)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request,'Bienvenido '+username_u+ ', has iniciado sesion ')
            return redirect('home')
        else:
            messages.error(request,'Usuario inactivo')
    else:
        messages.error(request,'El nombre de usuario y la contraseña que ingresaste no coinciden con nuestros registros. Por favor, revisa e inténtalo de nuevo.')
    return redirect('login')

def logout_view(request):

    logout(request)

    return redirect('home') 

def form_login(request):
    usuario = Usuario.objects.all()
    contexto ={
        "usuario":usuario,
    }

    return render(request,'puntos/inicio.html',contexto)

