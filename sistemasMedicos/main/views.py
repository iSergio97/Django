from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLogin, buscarArticulosCabecera, buscarNoticiasCabecera

from .models import Tema


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


def buscar_articulos(request):
    form = buscarArticulosCabecera()
    if request.method == 'POST':
        form = buscarArticulosCabecera(request.POST)
        if form.is_valid():
            temas = Tema.objects.get(cabecera=form.cleaned_data['cabecera'], category='Articulo')
    return render(request, 'articulos.html',
                  {'STATIC_URL': settings.STATIC_URL, 'path': 'register', temas: 'temas'})


def buscar_noticias(request):
    form = buscarArticulosCabecera()
    if request.method == 'POST':
        form = buscarArticulosCabecera(request.POST)
        if form.is_valid():
            temas = Tema.objects.get(cabecera=form.cleaned_data['cabecera'], category='Noticia')
    return render(request, 'noticias.html',
                  {'STATIC_URL': settings.STATIC_URL, 'path': 'register', temas: 'temas'})
