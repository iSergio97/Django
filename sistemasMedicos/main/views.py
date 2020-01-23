import ssl
import urllib.request

from bs4 import BeautifulSoup
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLogin, buscarTemasTitulo
from .models import Tema


# Create your views here.

def index(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'index'})


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


def populate_temas(request):
    def getElement(text, tag, clase):
        soup = BeautifulSoup(text, "html.parser")
        return soup.find_all(tag, class_=clase)

    def getElementNoClass(text, tag):
        soup = BeautifulSoup(text, "html.parser")
        return soup.find_all(tag)

    Tema.objects.all().delete()
    listaTemas = []
    id = 1
    sslC = ssl.SSLContext()

    for p in range(3):
        read = urllib.request.urlopen(url=("https://medicinaysaludpublica.com/categoria/noticias/page/" + str(p+1)),
                                      context=sslC)

        div = getElement(read, "div", ["content-archive-wrapper-1"])
        for i in div:
            article = getElement(str(i), "article",
                                 ["post", "type-post", "status-publish", "format-standard", "category-noticias"])
            for j in article:
                div1 = getElement(str(j), "div", ["entry-content"])
                for k in div1:
                    h2 = getElement(str(k), "h2", ["entry-post-title"])
                    for x in range(len(h2)):
                        a = h2[x].find("a")
                        title = a.string
                        link = a["href"]
                        category = "Noticia"

                        tema = Tema(id=id, titulo=title, link=link, category=category)
                        listaTemas.append(tema)
                        id = id + 1

    for p in range(3):
        read = urllib.request.urlopen("https://medicinaysaludpublica.com/categoria/articulos/page/" + str(p+1),
                                      context=sslC)

        div = getElement(read, "div", ["content-archive-wrapper-1"])
        for i in div:
            article = getElement(str(i), "article",
                                 ["post", "type-post", "status-publish", "format-standard", "category-articulos"])
            for j in article:
                div1 = getElement(str(j), "div", ["entry-content"])
                for k in div1:
                    h2 = getElement(str(k), "h2", ["entry-post-title"])
                    for x in range(len(h2)):
                        a = h2[x].find("a")
                        id = len(listaTemas) + 1
                        title = a.string
                        link = a["href"]
                        category = "Articulo"

                        tema = Tema(id=id, titulo=title, link=link, category=category)
                        listaTemas.append(tema)
                        id = id + 1

    Tema.objects.bulk_create(listaTemas)
    message = messages.success(request, "Se ha populado la base de datos de forma correcta")
    return render(request, 'populate.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'popular', message: 'messages'})


def buscar_articulos(request):
    form = buscarTemasTitulo()
    temas = ''
    if request.method == 'POST':
        form = buscarTemasTitulo(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            temas = Tema.objects.all().filter(titulo__contains=titulo, category='Articulo')
    return render(request, 'articulos.html',
                  {'temas': temas, 'STATIC_URL': settings.STATIC_URL, 'path': 'articulos'})


def buscar_noticias(request):
    form = buscarTemasTitulo()
    temas = ''
    if request.method == 'POST':
        form = buscarTemasTitulo(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            temas = Tema.objects.all().filter(titulo__contains=titulo, category='Noticia')

    return render(request, 'noticias.html',
                  {'temas': temas, 'STATIC_URL': settings.STATIC_URL, 'path': 'noticias'})
