# encoding:utf-8
from main.models import Evento
from main.forms import *
from django.shortcuts import render
from django.db.models import Avg
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
from datetime import datetime
import csv

import pandas

path = "data"

def index(request):
    populateEvents()
    return render(request, 'index.html', {'STATIC_URL': settings.STATIC_URL})


def populateEvents():
    print("Loading events")
    Evento.objects.all().delete()
    ruta = path + "\\dataset-C.csv"
#    fileobj = pandas.read_csv(ruta, error_bad_lines=False)
    lista = []
    with open(ruta, 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                splited = str(row).split(';')
                dateString =splited[2]
                dateDate = datetime.strptime(dateString, '%d/%m/%Y')
                precio = 0
                if splited[3] != 'Gratis':
                    precio = int(splited[3])
                evento = Evento(nombre=splited[0].replace('[\'', ''), tipo= splited[1],fechaInicio= dateDate, precio=precio, lenguajes=splited[4], municipio=splited[5], codigo=splited[6].replace('\']', ''))
                lista.append(evento)
            i += 1

    Evento.objects.bulk_create(lista)
    print("Populación completada con éxito")
    print("Se han cargado " + str(len(lista)) + " datos")


def mostrar_eventos_codigo(request):
    eventos =Evento.objects.all().order_by('codigo')
    return render(request, 'eventos_municipio.html', {'eventos':eventos, 'STATIC_URL':settings.STATIC_URL})


def buscarEventosPorIdioma(request):
    formulario = IdiomaBusquedaForm()
    eventos = None

    if request.method == 'POST':
        formulario = IdiomaBusquedaForm(request.POST)
        if formulario.is_valid():
            eventos = Evento.objects.all().filter(lenguajes__contains=formulario.cleaned_data['idioma'])

    return render(request, 'busqueda_idiomas.html', {'formulario': formulario, 'eventos': eventos, 'STATIC_URL': settings.STATIC_URL})


def buscarEventosPorFecha(request):
    formulario = EventoBusquedaYearForm()
    eventos = None

    if request.method == 'POST':
        formulario = EventoBusquedaYearForm(request.POST)
        if formulario.is_valid():
            fecha = datetime.strptime(formulario.cleaned_data['year'], '%d/%m/%Y')
            print(fecha)
            eventos = Evento.objects.all().filter(fechaInicio=fecha)

    return render(request, 'busqueda_fechas.html', {'formulario': formulario, 'eventos': eventos, 'STATIC_URL': settings.STATIC_URL})