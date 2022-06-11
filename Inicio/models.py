from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Configuracion(models.Model):
    logo=models.ImageField(upload_to='configuracion')
    telefono=models.CharField(max_length=20,null=True,blank=True)
    direccion=models.CharField(max_length=200,null=True,blank=True)
    facebook=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=120,null=True,blank=True)
    numero_clientes=models.IntegerField(default=1000)
    numero_corporativos=models.IntegerField(default=145)
    mision=models.TextField(null=True,blank=True)
    vision=models.TextField(null=True,blank=True)

    lunes_viernes_horario=models.CharField(max_length=50, null=True,blank=True)
    sabado_horario = models.CharField(max_length=50, null=True, blank=True)
    domingo_horario = models.CharField(max_length=50, null=True, blank=True)

    def imagen(self):
        return mark_safe('<img src="/media/%s" style="width: 100px" alt="Nodusnet">'%self.logo)

    class Meta:
        verbose_name_plural="Configuraciones"

class EventosProximos(models.Model):
    tipo=models.CharField(max_length=60, default="Recomendaciones", choices=(('Recomendaciones','Recomendaciones'),('Evento','Evento')))
    imagen=models.ImageField(upload_to='eventos')
    nombre_evento=models.CharField(max_length=100,help_text="Agasajo xxx xxx xxx",null=True,blank=True)
    fecha=models.TimeField(auto_now=True)
    fecha_iso = models.DateField(auto_now=True)
    descripcion=RichTextUploadingField()
    estado=models.BooleanField(default=True)
    visitas=models.IntegerField(default=0)
    resumen=models.TextField(default=" ",null=True,blank=True)

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



class Planes(models.Model):
    titulo=models.CharField(max_length=200)
    tipo=models.CharField(max_length=60)
    tecnologia=models.CharField(max_length=60)
    velocidad=models.CharField(max_length=60,default=" ")
    comparticion=models.CharField(max_length=20)
    precio_sin_impuesto=models.DecimalField(max_digits=9, decimal_places=2)
    precio_con_impuesto=models.DecimalField(max_digits=9, decimal_places=2)
    destacado=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Planes"

class Mi_empresa(models.Model):
    contenido=RichTextUploadingField()

    class Meta:
        verbose_name_plural="A cerca de Nosotros"

