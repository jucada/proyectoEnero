from django.db import models

# Create your models here.


class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)  #para mensajes de texto (cadenas de caracteres) pequeños
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=35)
    edad = models.IntegerField(default=0)