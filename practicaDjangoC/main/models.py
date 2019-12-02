#encoding:utf-8

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Evento(models.Model):
    nombre = models.TextField()
    tipo = models.TextField()
    fechaInicio = models.DateField()
    precio = models.IntegerField()
    lenguajes = models.TextField()
    municipio = models.TextField()
    codigo = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre', )