from django.contrib import admin
from recomendacion.models import *

# Register your models here.
admin.register(Etiqueta, Artista, UsuarioArtista, UsuarioEtiquetaArtista)