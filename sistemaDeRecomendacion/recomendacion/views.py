from django.shortcuts import render
from recomendacion.models import *
from django.conf import settings

# Create your views here.

path = 'data'

def index(request):
    populate()
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})

def populate():
    lista = []
    Etiqueta.objects.all().delete()
    ruta = path + "\\tags.dat"
    with open(ruta, 'r') as file:
        for line in file.readlines():
            lineSplited = str(line.split())
            idTag = lineSplited.split(",")[0].strip("['")
            tagValue = lineSplited.split(",")[1].strip("' ']")
            etiqueta = Etiqueta(idTag=float(int(idTag)), tagValue=tagValue)
            lista.append(etiqueta)

            Etiqueta.objects.bulk_create(lista)
            print(Etiqueta.objects.all().__sizeof__())
