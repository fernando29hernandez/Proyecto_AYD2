from django.db import models

# Create your models here.
class Tema(models.Model):
    Descripcion = models.CharField(max_length=255)
    Titulo = models.CharField(max_length=100)