from django.db import models

# Create your models here.
class Clientes(models.Model):
    cedula=models.CharField(max_length=13)
    nombres=models.CharField(max_length=60, null=True,blank=True)
    apellidos=models.CharField(max_length=60, null=True,blank=True)
    razon_social=models.CharField(max_length=300, null=True,blank=True)

    class Meta:
        verbose_name_plural="Clientes"

    def __str__(self):
        if not self.razon_social:
            return "%s %s"%(self.nombres,self.apellidos)
        else:
            return self.razon_social

class Pagos(models.Model):
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    descripcion=models.TextField()
    valor=models.DecimalField(default=0,decimal_places=2, max_digits=9)
    fecha=models.DateTimeField(auto_created=True,null=True,blank=True)
    fecha_pago=models.DateTimeField(auto_now=True,blank=True,null=True)
    estado=models.CharField(max_length=30)
