from django.db import models

# Create your models here.
'''
https://medicinaysaludpublica.com/categoria/articulos/

https://medicinaysaludpublica.com/categoria/noticias/
'''

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    email = models.EmailField()
    username = models.TextField(unique=True)
    contraseña = models.TextField()
    temasFavoritos = models.ManyToManyField('Tema', related_name='TemaFavoritoUsuario', blank=True)


class Foro(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()


class Tema(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.TextField()
    usuario = models.ForeignKey('Usuario', null=True)
    numRespuestas = models.IntegerField()
    ultimaRespuesta = models.DateField(null=True, blank=True)
    foroOrigen = models.ForeignKey('Foro', null=False)


class Respuesta(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey('Usuario', null=True)
    fechaHora = models.DateTimeField()
    texto = models.TextField()
    temaOrigen = models.ForeignKey('Tema', null=False)


class TemaFavoritoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey('Usuario')
    tema = models.ForeignKey('Tema')