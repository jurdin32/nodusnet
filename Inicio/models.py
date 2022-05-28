from django.db import models

# Create your models here.
class Configuracion(models.Model):
    logo=models.ImageField(upload_to='configuracion')



class Slider(models.Model):
    titulo=models.CharField(max_length=30, help_text="Texto de maximo 30 caracteres", default="NODUSNET")
    titulo2=models.CharField(max_length=100, help_text="Texto de maximo 100 caracteres", default="La velocidad que usted necesita")
    imagen=models.ImageField(upload_to='sliders',null=True,blank=True)
