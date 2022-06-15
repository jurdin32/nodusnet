from django.shortcuts import render

# Create your views here.
from Abonados.models import Pagos


def reporte_venta(request):
    pago=None
    if request.GET.get('id'):
        pago=Pagos.objects.get(id=request.GET.get('id'))
    print(pago.fecha_pago)
    contexto={
        'pago':pago,
    }
    return render(request,'reporte.html',contexto)