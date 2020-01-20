from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tema)
admin.site.register(TemaFavoritoUsuario)
admin.site.register(Respuesta)