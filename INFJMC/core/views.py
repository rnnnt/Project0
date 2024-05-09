from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hola mundo")

def carreras(request):
    return HttpResponse("carreras")

def docentes(request):
    return HttpResponse("docentes")