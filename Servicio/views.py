from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioServicio

# Create your views here.

def inicio_admin(request):
    return render(request, 'inicio_admin.html')


def registrar_admin(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                    )
                admin_group = Group.objects.get(name='administrador')  # Asume que el grupo existe
                usuario.groups.add(admin_group)
                usuario.save()
                return redirect('inicio_admin')
        except IntegrityError:
            return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : 'El usuario ya existe'})
    return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : "Contraseñas no coinciden"
        })

def crear_servicio(request):
    if request.method == 'POST':
        form = FormularioServicio(request.POST)
        servicio = form.save(commit=False)
        servicio.save()
        return redirect('inicio_admin')
    return render(request, 'crear_servicio.html',{
        'form' : FormularioServicio()
    })