from django.shortcuts import render, redirect
from .models import Usuario, Tipo_usuario, Comuna, Centro, Vacuna,DireccionC, DireccionU, Contacto
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
	return render(request, 'puntos/home.html')

def inicio(request):
	return render(request, 'puntos/inicio.html')

def contacto(request):
    return render(request, 'puntos/Contacto.html')

def centros(request):
    comunas = Comuna.objects.all()
    centros = Centro.objects.all()
    contexto = {
        "comunas": comunas,
        "centros": centros,
    }
    
    return render (request,'puntos/centros.html',contexto)

def contac(request):
    nombre_c = request.POST['Nombre']
    apellido_c = request.POST['Apellido']
    correo_c = request.POST['correo']
    asunto_c = request.POST['Asunto']
    comentario_c = request.POST['com']

    Contacto.objects.create(nombre = nombre_c,apellido = apellido_c,correo = correo_c,comentario = comentario_c , asunto = asunto_c)

    messages.success(request,'Mensaje enviado exitosamente.')

    return redirect('contacto') 
	

def lista_usuarios(request):
	usuario = Usuario.objects.all()
	usuarios = Usuario.objects.all()
	contexto ={
        "usuario":usuario,
	    "Usuarios":usuarios,
       
    }
	return render(request, 'puntos/lista_usuarios.html',contexto)


def registrar(request):
	return render(request, 'puntos/registrar.html')



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



def modificar_usuario(request,id):
    usuario1 = Usuario.objects.get(user_id = id)
    tipos1 = Tipo_usuario.objects.all()
    usuario = Usuario.objects.all()

    contexto={
        "usuario_modificar":usuario1,
        "tipos_usuarios":tipos1,
        "usuario":usuario,


    }
    return render(request,'puntos/modificar_usuario.html',contexto)
	


def modificar_us(request):
    id_usr=request.POST['id_usr']
    nombre_us=request.POST['Nombre']
    rut_us=request.POST['Rut']
    correo_us=request.POST['correo']
    us_username = request.POST['Username']
    us_tipo = request.POST['tipu']
    us_tipos = Tipo_usuario.objects.get(id_tipo_usuario = us_tipo)

    usuario_p= Usuario.objects.get(num_run= rut_us)
    usuario_p.nombres = nombre_us
    usuario_p.correo = correo_us
    usuario_p.tipo_usuario = us_tipos
    usuario_p.nombre_usr = us_username
    usuario_p.save()

    usuario_usr = User.objects.get(id = id_usr)
    if Usuario.objects.filter(tipo_usuario = 1):
        usuario_usr.is_superuser = True
        usuario_usr.is_staff = True

    elif Usuario.objects.filter(tipo_usuario = 2):
        usuario_usr.is_superuser = False
        usuario_usr.is_staff = False
    
    usuario_usr.save()
    messages.success(request,'**El usuario '+us_username+' a sido modificado exitosamente.**')
    return redirect('lista_usuarios')


def eliminar_usuario(request, id):
    usu = Usuario.objects.get(user_id = id)
    usu.delete()
    usu1 = User.objects.get(id = id)
    usu1.delete()
    messages.success(request,'**El usuario '+usu.nombre_usr+' a sido eliminado exitosalemte.**')

    return redirect('lista_usuarios')

def buscar_usuario(request):
    if Usuario.nombre_usr:
        x = request.POST['buscar_us']
        u1 = Usuario.objects.filter(nombre_usr__contains = x )
        u2 = Usuario.objects.filter(num_run__contains = x )
        usuario = Usuario.objects.all()

        contexto = {
            "us1" : u1 or u2,
            "usuario":usuario,
            }
        messages.success(request,'Resultados de: '+x)
    return render(request,'puntos/lista_usuarios.html', contexto )

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


def registrar_usuario(request):
    tipo_usuario = Tipo_usuario.objects.all()
    contexto ={
        "tipo_usuario":tipo_usuario,
    }

    return render(request,'puntos/registrar_usuario.html',contexto)

def registrar2(request):
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
        return redirect('registrar')

    except User.DoesNotExist:
        try:
            b=Usuario.objects.get(num_run=rut_u)
            messages.error(request,'El Rut no esta disponible')
            return redirect('registrar')

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
            
                return redirect('home')
            else:
                messages.error(request,'La contraseña no coinside')    
                return redirect('registrar')


def registrar_centro(request):
    comunas = Comuna.objects.all()
    contexto = {"comunas": comunas}
    return render(request,'puntos/registrar_centro.html',contexto)

def registrar_comuna(request):
    
    return render(request,'puntos/registrar_comuna.html')



def lista_centros(request):
    centrosa = Centro.objects.all()
    contexto = {"Centros": centrosa}
    return render(request,'puntos/lista_centros.html', contexto)


def guardar_comuna(request):
    nom_com = request.POST['Nombre']
   

    Comuna.objects.create(nombre = nom_com)
    messages.success(request, "Comuna agregada correctamente")
    return redirect('lista_centros')





def guardar_centro(request):
    nom_cen = request.POST['nom_cent']
    des_cen = request.POST['des_cent']
    com = request.POST['comuna']
    dire = request.POST['direc']
    com2 = Comuna.objects.get(id_comuna = com)
    Centro.objects.create(nombre = nom_cen, descripcion = des_cen, direccion = dire , comuna = com2)

    messages.success(request, "Centro Agregado exitosamente")
    return redirect('lista_centros')


def eliminar_centro(request, id):
    centros = Centro.objects.get(id_centro = id)
    centros.delete()
    messages.success(request,'Centro Eliminado')

    return redirect('lista_centros')



def modificar_centro(request, id):
    centro1 = Centro.objects.get(id_centro = id)
    comunas = Comuna.objects.all()
   
    contexto = {
        "modificar_centro":centro1,
        "comunas":comunas
    }
    return render(request,'puntos/modificar_centro.html',contexto)






def buscar_centro(request):
    if Centro.nombre:
        x = request.POST['b_centro']
        c1 = Centro.objects.filter(nombre__contains = x )
        
        centros = Centro.objects.all()

        contexto = {
            "cn1" : c1, 
            "cn2": centros
            

            
            }
        messages.success(request,'Resultados de: '+x)
    return render(request,'puntos/lista_centros.html', contexto )



    #   def buscar_usuario(request):
    # if Usuario.nombre_usr:
    #     x = request.POST['buscar_us']
    #     u1 = Usuario.objects.filter(nombre_usr__contains = x )
    #     u2 = Usuario.objects.filter(num_run__contains = x )
    #     usuario = Usuario.objects.all()

    #     contexto = {
    #         "us1" : u1 or u2,
    #         "usuario":usuario,
    #         }
    #     messages.success(request,'Resultados de: '+x)
    # return render(request,'puntos/lista_usuarios.html', contexto )


#vacuna
def registrar_vacuna(request):
   return render(request,'puntos/registrar_vacuna.html')

def guardar_vacuna(request):
    nom_vac = request.POST['nom_vacu']
    lab_vac = request.POST['lab_vacu']
    des_vac = request.POST['des_vacu']
    
    Vacuna.objects.create(nombre = nom_vac, lab = lab_vac, descripcion = des_vac)
    messages.success(request, "Vacuna Agregado exitosamente")
    return redirect('lista_vacunas')


def eliminar_vacuna(request, id):
    vacunas = Vacuna.objects.get(id_vacuna = id)
    vacunas.delete()
    messages.success(request,'vacuna Eliminada')

    return redirect('lista_vacunas')

def lista_vacunas(request):
    vacunasx = Vacuna.objects.all()
    contexto = {"vacu": vacunasx}
    return render(request,'puntos/lista_vacunas.html', contexto)

def modificar_vacuna(request, id):
    vacuna11 = Vacuna.objects.get(id_vacuna = id)
   
    contexto = {
        "modificar_vacuna":vacuna11
    }
    return render(request,'puntos/modificar_vacuna.html',contexto)

def funcionmodvac(request):
    id_vac = request.POST['id_vacu']
    nom_vac = request.POST['nom_vacu']
    lab_vac = request.POST['lab_vacu']
    des_vac = request.POST['des_vacu']
   

    vacuna1 = Vacuna.objects.get(id_vacuna = id_vac)
    vacuna1.nombre = nom_vac
    vacuna1.lab = lab_vac
    vacuna1.descripcion = des_vac

    
    vacuna1.save()

    messages.success(request, 'Vacuna  modificada')
    return redirect('lista_vacunas')

def funcionmodcen(request):
    id_cen = request.POST['id_cent']
    nom_cen = request.POST['nom_cent']
    des_cen = request.POST['des_cent']
    com = request.POST['comuna']
    dire = request.POST['direc']
    com_2 = Comuna.objects.get(id_comuna = com)
   

    centro1 = Centro.objects.get(id_centro = id_cen)
    centro1.nombre = nom_cen
    centro1.descripcion = des_cen
    centro1.comuna = com_2
    centro1.direccion = dire
   

    
    centro1.save()

    messages.success(request, 'Centro modificado correctamente')
    return redirect('lista_centros')

def buscar_vacuna(request):
    if Vacuna.nombre:
        x = request.POST['b_vacuna']
        v1 = Vacuna.objects.filter(nombre__contains = x )
        
        vacunas = Vacuna.objects.all()

        contexto = {
            "vn1" : v1, 
            "vn2": vacunas
            

            
            }
        messages.success(request,'Resultados de: '+x)
    return render(request,'puntos/lista_vacunas.html', contexto )
