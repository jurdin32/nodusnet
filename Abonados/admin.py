from django.contrib import admin

# Register your models here.
from Abonados.models import *
from nodusnet.snniper import Attr


@admin.register(Clientes)
class modelo (admin.ModelAdmin):
    list_display = Attr(Clientes)
    list_display_links = Attr(Clientes)

@admin.register(Pagos)
class modelo (admin.ModelAdmin):
    list_display = Attr(Pagos)
    list_display_links = Attr(Pagos)