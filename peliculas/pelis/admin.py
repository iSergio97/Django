from django.contrib import admin
from .models import Usuario, Pelicula, Director

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Director)
