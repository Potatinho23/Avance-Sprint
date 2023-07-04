from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import FormularioUsuario, FormularioLogin
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'tienda/index.html')

def abogado(request):
    return render(request, 'tienda/abogado.html')


def acercade(request):
    return render(request, 'tienda/acercade.html')


@login_required
def perfil(request):
    return render(request, 'tienda/perfil.html')


def inicio_sesion(request):
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password1')
            usuario = authenticate(username=nombre_usuario, password1=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect(to='perfil')
    return render(request, 'registration/login.html',)


def registro(request):
    data = {
        'form':FormularioUsuario()
    }

    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        
    return render(request, 'registration/registro.html', data)

def exit(request):
    logout(request)
    return redirect('/')


@login_required
def eliminar_usuario(request):
    user = request.user
    try:
        user = User.objects.get(username=user.username)
        user.is_active = False
        user.save()
        return redirect('login')
    except User.DoesNotExist:
        return redirect('login')
    
@login_required
def modificar_datos(request, username):
    
    usuario = get_object_or_404(User, username = username)

    data = {
        'form':FormularioUsuario(instance=usuario)
    }

    if request.method == 'POST':
        formulario = FormularioUsuario(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='perfil')
        data['form'] = formulario
    return render(request, 'tienda/modificar.html', data)


