from django.contrib import admin

# Register your models here.
from Inicio.models import *
from nodusnet.snniper import Attr

@admin.register(Configuracion)
class modelo (admin.ModelAdmin):
    list_display = Attr(Configuracion)
    list_display_links = Attr(Configuracion)

@admin.register(Slider)
class modelo (admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)
