from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

# Create your models here.

def inicio(request):
    return render_to_response('index.html', {})