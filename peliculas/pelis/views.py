from django.shortcuts import render
from .models import Usuario, Director, Pelicula
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# Create your views here.

#Si lo que queremos enviar es texto plano, debemos enviar el texto como un HttpResponse


def sobre(request):
    html = "<htlm> <body> Ejemplo en sobre </body></html>"
    return HttpResponse(html)


#Preguntar cómo definir una página de inicio
def inicio(request):
    return render_to_response('inicio.html', {})

# TODO: Arreglar problema de inicio.html
# No se consigue filtrar información a través de un if/endif en la vista para listar en función de un dato
# El dato accion pasa siempre a la vista como users. Revisar el porqué

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuarios, "accion": "users"})

def peliculas(request):
    directores = Director.objects.all()
    return render_to_response('peliculas.html', {'directores': directores, "accion": "directores"})

def directores(request):
    peliculas = Pelicula.objects.all()
    return render_to_response('directores.html', {'pelicula': peliculas, "accion": "peliculas"})