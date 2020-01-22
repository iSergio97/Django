from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from .forms import UserLogin, UserRegisterForm
from .models import Usuario, Tema


# Create your views here.


def index(request):
    current_user = request.user
    print(current_user)
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'index'})


def articulos(request):
    return render(request, 'articulos.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'articulos'})


def noticias(request):
    return render(request, 'noticias.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'noticias'})


def login_view(request):
    form = UserLogin()
    message = ''
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            form.clean()
            username = form.cleaned_data['username']
            password = form.cleaned_data['contraseña']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = messages.success(request, "Ha iniciado sesión con éxito")
                return redirect('/')
            else:
                message = messages.error(request, "No existe un usuario con ese username y con esa contraseña")

    return render(request, 'login.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'login', message: 'messages'})


def logout_view(request):
    message: ''
    if request.user != 'AnonymousUser':
        logout(request)
        message = messages.success(request, "Ha cerrado sesión de forma correcta")
        return redirect("/")
    else:
        message = messages.error(request, "No puede cerrar sesión si no ha iniciado antes sesión")
        return redirect("login/")


def register_view(request):
    form = UserRegisterForm()
    message = ''
    print(request.user)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['nombre']
            print(nombre)
            apellido = form.cleaned_data['apellido']
            print(apellido)
            email = form.cleaned_data['email']
            print(email)
            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['contraseña']
            print(password)
            user = ''
            try:
                user = Usuario.objects.get(username=username)
                message = messages.error(request, "Ya existe un usuario con ese nombre de usuario")
            except Usuario.DoesNotExist:
                user = Usuario.objects.create(nombre=nombre, apellido=apellido, email=email, username=username,
                                              contraseña=password).save()
                message = messages.success(request, "Ha iniciado sesión con éxito")
                return redirect('/')

    return render(request, 'register.html',
                  {'STATIC_URL': settings.STATIC_URL, 'path': 'register', message: 'messages'})


def viewArticle(request):
    query = request.GET.get('id')
    tema = Tema.objects.get(id=query)
    return render(request, 'articulos.html',
                  {'STATIC_URL': settings.STATIC_URL, 'path': 'register', tema: 'tema'})



def viewNotice(request):
    query = request.GET.get('id')
    tema = Tema.objects.get(id=query)
    return render(request, 'noticias.html.html',
                  {'STATIC_URL': settings.STATIC_URL, 'path': 'register', tema: 'tema'})