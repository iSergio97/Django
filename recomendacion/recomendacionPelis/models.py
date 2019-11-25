from django.db import models

# Create your models here.

class Pelicula(models.Model):
    idPelicula = models.IntegerField(primary_key= True)
    titulo = models.CharField(max_length=100)
    fechaEstreno = models.DateField()
    IMDbURL = models.URLField()


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=50)
    pelicula = models.ManyToManyField(Pelicula)

class Puntuacion(models.Model):
    usuario = models.ForeignKey(Usuario)
    pelicula = models.ForeignKey(Pelicula)