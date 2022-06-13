from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Abonados.models import Pagos, Clientes
from BotonPagos.models import PagoWeb
from ConfiguracionEmail.enviar_email import enviarEmail
from Inicio.models import Configuracion, EventosProximos, Slider, Planes, Mi_empresa


def index(request):
    configuracion=Configuracion.objects.last()
    sliders=Slider.objects.all()
    contexto={
        'sliders':sliders,
        'configuracion':configuracion,
        'eventos':EventosProximos.objects.filter(estado=True).order_by('fecha_modificacion'),
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
    configuracion=Configuracion.objects.last()
    contexto={
        'configuracion':configuracion
    }
    print(request.POST)
    if request.POST:
        enviarEmail(destinatarios=[request.POST.get('email')], asunto="Nodusnetsa.ec",
                    mensaje="Gracias por ponerte en contacto con nosotros en breve atenderemos tu requerimiento", is_html=False)
        enviarEmail(destinatarios=[configuracion.email], asunto="Un Usuario trata de ponerse en contacto desde Nodusnetsa.ec",
                    mensaje=request.POST.get('subject')+"\n"+request.POST.get('message'),
                    is_html=False)
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
    cliente=None
    try:
        pago=Pagos.objects.get(id=id)
        cliente=pago.cliente.cedula
        pago.estado="Pagado"
        pago.referencia=request.GET.get('id')
        pago.save()
        enviarEmail(destinatarios=[pago.cliente.email], asunto="Nodusnet Comprobante de transaccion", mensaje="Nodusnet le agradece su pago por: %s desde nuestra plafaforma web, si tiene dudas puede consultar sus valores a pagar en: https://nodusnetsa.ec/cash?cliente=%s"%(pago.valor, pago.cliente.cedula), is_html=False)
    except Exception as error:
        print(error)
    print(request.GET)
    return HttpResponseRedirect("/cash/?cliente=%s"%cliente)