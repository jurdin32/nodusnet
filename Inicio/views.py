from django.shortcuts import render

# Create your views here.
from Inicio.models import Configuracion, EventosProximos


def index(request):
    contexto={
        'configuracion':Configuracion.objects.last(),
        'eventos':EventosProximos.objects.all(),
    }
    return render(request,"index-corporate.html",contexto)

def nosotros(request):
    contexto={
        'configuracion':Configuracion.objects.last()
    }
    return render(request,"index-corporate.html",contexto)

def planes(request):
    contexto={
        'configuracion':Configuracion.objects.last()
    }
    return render(request,"index-corporate.html",contexto)

def contacto(request):
    contexto={
        'configuracion':Configuracion.objects.last()
    }
    return render(request,"index-corporate.html",contexto)