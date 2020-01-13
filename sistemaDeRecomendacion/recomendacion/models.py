from django.db import models


# Create your models here.

class Artista(models.Model):
    idArtista = models.IntegerField()
    nombre = models.TextField()
    url = models.URLField()
    pictureURL = models.URLField()


class Etiqueta(models.Model):
    idTag = models.BigIntegerField(primary_key=True)
    tagValue = models.TextField()


class UsuarioArtista(models.Model):
    idUsuario = models.IntegerField()
    idArtista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    tiempoEscucha = models.BigIntegerField()


class UsuarioEtiquetaArtista(models.Model):
    idUsuario = models.IntegerField()
    idArtista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    idTag = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
