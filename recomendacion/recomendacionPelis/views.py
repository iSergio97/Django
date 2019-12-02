from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse


def inicio(request):
    read = open("../recomendacion/recomendacion/text.txt", "r")
    for line in read:
        print(line)
    return render_to_response('index.html', {})

