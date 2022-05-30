from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Configuracion(models.Model):
    logo=models.ImageField(upload_to='configuracion')
    telefono=models.CharField(max_length=12,null=True,blank=True)
    email=models.EmailField(max_length=120,null=True,blank=True)
    numero_clientes=models.IntegerField(default=1000)
    numero_corporativos=models.IntegerField(default=145)
    mision=models.TextField(null=True,blank=True)
    vision=models.TextField(null=True,blank=True)

    def imagen(self):
        return mark_safe('<img src="/media/%s" style="width: 100px" alt="Nodusnet">'%self.logo)

    class Meta:
        verbose_name_plural="Configuraciones"

class EventosProximos(models.Model):
    imagen=models.ImageField(upload_to='eventos')
    nombre_evento=models.CharField(max_length=30,help_text="Agasajo xxx xxx xxx",null=True,blank=True)
    fecha=models.TimeField(auto_now=True)
    fecha_iso = models.DateField(auto_now=True)
    descripcion=models.TextField(null=True,blank=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="Eventos"


class Slider(models.Model):
    titulo1=models.CharField(max_length=50, null=True,blank=True, help_text="Texto de maximo 50 caracteres", default="La velocidad que usted necesita")
    titulo2=models.CharField(max_length=30, null=True,blank=True, help_text="Texto de maximo 30 caracteres", default="NODUSNET")
    titulo3 = models.CharField(max_length=100, null=True,blank=True, help_text="Texto de maximo 100 caracteres", default="NODUSNET")
    imagen=models.ImageField(upload_to='sliders',null=True,blank=True)
    color=models.CharField(max_length=30,null=True,blank=True, help_text="En formato hexadecimal")

    class Meta:
        verbose_name_plural="Sliders"
