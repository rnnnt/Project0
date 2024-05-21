from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo_carrera = models.CharField(max_length=10, verbose_name='codigo')
    nombre = models.CharField(max_length=80, verbose_name='nombre')
    duracion = models.IntegerField(verbose_name='duracion', default=1) #min=0

    def __str__(self) -> str:
        return self.nombre