from django.contrib import admin

# Register your models here.
from Inicio.models import *
from nodusnet.snniper import Attr

@admin.register(Configuracion)
class modelo (admin.ModelAdmin):
    list_display = Attr(Configuracion)+['imagen']
    list_display_links = Attr(Configuracion)+['imagen']

@admin.register(EventosProximos)
class modelo (admin.ModelAdmin):
    list_display = Attr(EventosProximos)
    list_display_links = Attr(EventosProximos)

@admin.register(Slider)
class modelo (admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)
