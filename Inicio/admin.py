from django.contrib import admin

# Register your models here.
from Inicio.models import Slider
from nodusnet.snniper import Attr

@admin.register(Slider)
class modelo (admin.ModelAdmin):
    list_display = Attr(Slider)
    list_display_links = Attr(Slider)
