from django.db import models

# Create your models here.

class Anime(models.Model):
    animeId = models.BigIntegerField(primary_key=True)
    titulo = models.TextField()
    generos = models.TextField()
    formatoEmision = models.TextField()
    numEpisodios = models.TextField()


class Puntuacion(models.Model):
    idUsuario = models.BigIntegerField()
    animeId = models.ForeignKey("Anime", on_delete=models.CASCADE)
    puntuacionValor = models.IntegerField()