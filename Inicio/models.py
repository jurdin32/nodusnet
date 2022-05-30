from django.db import models

# Create your models here.
class Configuracion(models.Model):
    logo=models.ImageField(upload_to='configuracion')
    telefono=models.CharField(max_length=12,null=True,blank=True)



class Slider(models.Model):
    titulo1=models.CharField(max_length=50, null=True,blank=True, help_text="Texto de maximo 50 caracteres", default="La velocidad que usted necesita")
    titulo2=models.CharField(max_length=30, null=True,blank=True, help_text="Texto de maximo 30 caracteres", default="NODUSNET")
    titulo3 = models.CharField(max_length=100, null=True,blank=True, help_text="Texto de maximo 100 caracteres", default="NODUSNET")
    imagen=models.ImageField(upload_to='sliders',null=True,blank=True)
    color=models.CharField(max_length=30,null=True,blank=True, help_text="En formato hexadecimal")
