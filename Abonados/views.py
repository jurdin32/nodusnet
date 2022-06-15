from django.shortcuts import render

# Create your views here.
from Abonados.models import Pagos
from Inicio.models import Configuracion


def reporte_venta(request):
    pago=None
    if request.GET.get('id'):
        pago=Pagos.objects.get(id=request.GET.get('id'))
    print(pago.fecha_pago)
    contexto={
        'pago':pago,
        'configuracion':Configuracion.objects.last()
    }
    return render(request,'reporte.html',contexto)