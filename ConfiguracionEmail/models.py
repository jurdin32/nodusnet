from django.db import models

# Create your models here.
class EnvioEmail(models.Model):
    servidor_smtp=models.CharField(max_length=60)
    puerto=models.IntegerField(default=587)
    use_tls: models.BooleanField(default=True)
    usuario: models.CharField(max_length=200, default='urdin-23@live.com')
    password:models.CharField(max_length=200, default="Urdin32**")