from django.contrib import admin

# Register your models here.
from ConfiguracionEmail.models import EnvioEmail
from nodusnet.snniper import Attr


@admin.register(EnvioEmail)
class modelo(admin.ModelAdmin):
    list_display = Attr(EnvioEmail)
    list_display_links = Attr(EnvioEmail)