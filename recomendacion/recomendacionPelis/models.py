from django.db import models

# Create your models here.

class Pelicula(models.Model):
    idPelicula = models.IntegerField(primary_key= True)
    titulo = models.CharField(max_length=100)
    fechaEstreno = models.DateField()
    IMDbURL = models.URLField()
    categorias =


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=50)

class Ocupacion(models.Model):
    nombre = models.CharField(max_length= 50)

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key= True)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    codigoPostal = models.IntegerField()



