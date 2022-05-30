from django.shortcuts import render

# Create your views here.
from Inicio.models import Configuracion


def index(request):
    contexto={
        'configuracion':Configuracion.objects.last()
    }
    return render(request,"index-corporate.html",contexto)