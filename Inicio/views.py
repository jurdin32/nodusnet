from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Inicio.models import Configuracion, EventosProximos, Slider, Planes, Mi_empresa


def index(request):
    configuracion=Configuracion.objects.last()
    sliders=Slider.objects.all()
    contexto={
        'sliders':sliders,
        'configuracion':configuracion,
        'eventos':EventosProximos.objects.all().order_by('-id'),
    }
    return render(request,"index-corporate.html",contexto)

def nosotros(request):
    contexto={
        'configuracion':Configuracion.objects.last(),
        'empresa':Mi_empresa.objects.last(),
    }
    return render(request,"nosotros.html",contexto)

def planes(request):
    contexto={
        'configuracion':Configuracion.objects.last(),
        'planes':Planes.objects.all(),
    }
    return render(request,"planes.html",contexto)

def contacto(request):
    contexto={
        'configuracion':Configuracion.objects.last()
    }
    return render(request,"contacto.html",contexto)

def eventos(request):
    event=EventosProximos.objects.get(id=request.GET.get('event'))
    event.visitas+=1
    event.save()
    contexto={
        'configuracion':Configuracion.objects.last(),
        'eventos':event,
    }
    return render(request,"blog-post.html",contexto)


def politicas(request):
    contexto={
        'configuracion': Configuracion.objects.last(),
    }
    return render(request,'politicas.html',contexto)

def velocidad(request):
    contexto={
        'configuracion': Configuracion.objects.last(),
    }
    return render(request,'velocidad.html',contexto)

def prueba_pagos(request):

    return render(request,'prueba_pago.html')

def pago_ok(request):
    return render(request,'pagos_ok.html')