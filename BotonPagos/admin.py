from django.contrib import admin

# Register your models here.
from BotonPagos.models import PagoWeb
from nodusnet.snniper import Attr


@admin.register(PagoWeb)
class modelo(admin.ModelAdmin):
    list_display = Attr(PagoWeb)
    list_display_links = Attr(PagoWeb)