from .models import *
from django.shortcuts import render
from django.conf import settings
import csv
from .forms import *
from django.db.models import F, Q, Exists, Value, IntegerField, Sum, Count


path = "data"


def index(request):
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})

def populate(request):
    populateAnimes()
    populatePuntuaciones()
    return render(request, 'populate.html', {'STATIC_URL': settings.STATIC_URL})

def buscarAnimesPorGenero(request):
    formulario = IdAnimeFormulario()
    animes = None

    if request.method == 'POST':
        formulario = IdAnimeFormulario(request.POST)
        if formulario.is_valid():
            animes = Anime.objects.all().filter(generos__contains=formulario.cleaned_data["genero"])

    return render(request, 'busqueda_genero.html', {'formulario': formulario, 'animes': animes, 'STATIC_URL': settings.STATIC_URL})

def buscarAnimeMejorValorado(request):
    puntuacion = Puntuacion.objects.annotate(puntuacion=Count('puntuacionValor')).order_by('-puntuacionValor')[:2]
    anime1 = Anime.objects.get(animeId=puntuacion[0].animeId.animeId)
    anime2 = Anime.objects.get(animeId=puntuacion[1].animeId.animeId)

    return render(request, 'mejor_anime.html', {"anime1": anime1, "anime2": anime2, 'STATIC_URL': settings.STATIC_URL})

def populateAnimes():
    Anime.objects.all().delete()

    ruta = path + "\\anime.csv"
    listaAnimes = []
    with open(ruta, 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                splitted = str(row).split(";")
                animeId = splitted[0].replace('[\'', '')
                titulo = splitted[1]
                generos = splitted[2]
                formatoEmision = splitted[3]
                numEpisodios = splitted[4].replace('\']', '')

                anime = Anime(animeId=animeId, titulo=titulo, generos=generos, formatoEmision=formatoEmision, numEpisodios=numEpisodios)
                listaAnimes.append(anime)

            i+=1

        Anime.objects.bulk_create(listaAnimes)


def populatePuntuaciones():
    Puntuacion.objects.all().delete()

    ruta = path + "\\ratings.csv"
    listaRatings = []
    with open(ruta, 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                splitted = str(row).split(";")
                userId = splitted[0].replace('[\'', '')
                animeId = splitted[1]
                rating = splitted[2].replace('\']', '')
                anime = Anime.objects.get(animeId=animeId)

                puntuacion = Puntuacion(animeId=anime, idUsuario=userId, puntuacionValor=rating)
                listaRatings.append(puntuacion)

            i += 1

        Puntuacion.objects.bulk_create(listaRatings)