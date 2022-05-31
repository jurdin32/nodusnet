from django.shortcuts import render

# Create your views here.
from Inicio.models import Configuracion, EventosProximos, Slider


def index(request):
    configuracion=Configuracion.objects.last()
    sliders=Slider.objects.all()
    contexto={
        'sliders':sliders,
        'configuracion':configuracion,
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
    return render(request,"contacto.html",contexto)