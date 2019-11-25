from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    apellidos = models.TextField()
    fechaNacimiento = models.DateField()
    categoria = models.CharField(max_length=20)

    def __unicode__(self):
        return self.apellidos, self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length=15)
    apellidos = models.TextField()
    biografia = models.TextField()

    def __unicode__(self):
        return self.apellidos, self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=20)
    estreno = models.IntegerField()
    resumen = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    categoria = models.CharField(max_length=15)

    def __unicode__(self):
        return self.titulo, "(", self.estreno, ")"
