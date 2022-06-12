from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Abonados.models import Pagos, Clientes
from BotonPagos.models import PagoWeb
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
    pagos=None
    cliente=None
    try:
        cliente=Clientes.objects.get(cedula=request.GET.get('cliente'))
        pagos = Pagos.objects.filter(cliente=cliente).order_by("-fecha")
    except:
        cliente="Cliente no registrado en la base de datos"

    contexto={
        'configuracion':Configuracion.objects.last(),
        'pago':PagoWeb.objects.last(),
        'deudas':pagos,
        'cliente':cliente,
    }
    return render(request,'prueba_pago.html',contexto)

def pago_ok(request):
    id=request.GET.get('clientTransactionId').replace("NODUSNET-","")
    pago=Pagos.objects.get(id=id)
    cliente=pago.cliente.cedula
    pago.estado="Pagado"
    pago.referencia=request.GET.get('id')
    pago.save()
    print(request.GET)
    return HttpResponseRedirect("/cash/?cliente=%s"%cliente)