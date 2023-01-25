from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor

# Create your views here.

def inicio(request):

    return HttpResponse("Hola, bienvienido a mi página.")


def agregar_profe(request):

    profe1 = Profesor(nombre="Pepe", apellido="Perez", email = "pepe@perez.la", profesion="Desarrollador de Apps", edad=25)
    profe1.save()

    return HttpResponse(f"Hemos creado al profesor {profe1.nombre} a la base de datos.")