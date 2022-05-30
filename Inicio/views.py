from django.shortcuts import render

# Create your views here.
from Inicio.models import Configuracion, EventosProximos

def llenado_informacion(request):
    configuracion = Configuracion.objects.last()
    print(configuracion)
    if configuracion:
        if configuracion.logo:
            request.session["logo"] = "/media/%s" % str(configuracion.logo)
        if configuracion.telefono:
            request.session["telefono"] = configuracion.telefono
        if configuracion.facebook:
            request.session["facebook"] = configuracion.facebook
        if configuracion.email:
            request.session["email"] = configuracion.email
        if configuracion.numero_clientes:
            request.session["numero_clientes"] = configuracion.numero_clientes
        if configuracion.numero_corporativos:
            request.session["numero_corporativos"] = configuracion.numero_corporativos


def index(request):
    configuracion=Configuracion.objects.last()
    llenado_informacion(request)

    contexto={
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
    return render(request,"index-corporate.html",contexto)