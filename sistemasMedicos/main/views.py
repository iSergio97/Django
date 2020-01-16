from django.shortcuts import render
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'index'})

def articulos(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'articulos'})

def noticias(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL, 'path': 'noticias'})