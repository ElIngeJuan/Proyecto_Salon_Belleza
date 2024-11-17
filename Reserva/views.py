from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import redirect
from .forms import FormularioReserva
from .models import Reserva

# Create your views here.

def registrar_usuario(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                    )
                cliente_group = Group.objects.get(name='Cliente')  # Asume que el grupo existe
                usuario.groups.add(cliente_group)
                usuario.save()
                return redirect('login_usuario')
        except IntegrityError:
            return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : 'El usuario ya existe'})
    return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : "Contraseñas no coinciden"
        })

def login_usuario(request):
    if request.method == 'POST':
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio_cliente')
        else:
            return render(request, 'inicio_sesion.html', {
                'form' : AuthenticationForm(),
                'error' : 'Usuario o contraseña incorrectos'
            })
    return render(request, 'inicio_sesion.html', {
        'form' : AuthenticationForm()
    })

def log_out_user(request):
    logout(request)
    return redirect('inicio_cliente')

def inicio_cliente(request):
    return render(request, 'inicio_cliente.html')

def create_servicio(request):
    if request.method == 'POST':
        form = FormularioReserva(request.POST)
        reserva = form.save(commit=False)
        reserva.usuario = request.user
        reserva.save()
        return render(request, 'crear_reserva.html', {
            'form': FormularioReserva(),
            'titulo': 'Crear Reserva',
        })
    return render(request, 'crear_reserva.html', {
        'form': FormularioReserva(),
        'titulo': 'Crear Reserva',
    })

def ver_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'ver_reserva.html', {
        'reservas': reservas
    })

def reserva_detalle(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'reserva_detalle.html', {
        'reserva': reserva
    })

def actualizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    form = FormularioReserva(request.POST or None, instance=reserva)
    if form.is_valid():
        form.save()
        return redirect('ver_reservas')
    return render(request, 'crear_reserva.html', {
        'form': form,
        'titulo': 'Actualizar Reserva'
    })

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == 'POST':
        reserva.delete()
    return redirect('ver_reservas')