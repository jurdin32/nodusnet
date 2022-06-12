from django.db import models

# Create your models here.
class PagoWeb(models.Model):
    storeid=models.CharField(max_length=200,default="2f510795-5ee5-48a7-a182-8b239191e251")
    token=models.TextField(default="bhdcVxutdPvAFeUBUa4u93Ero0U7J4NPC3DLJ-kzww5ZSWMDc3aWI5IabyMqHcWc64U4q-HElHlqxRVq0ALlob2cfXQQ-58dLRIAh_KAANhjW30nr6qR87pzazFVYhUnmQtzkR9ccqRzIFypQDxEANFm1beAUSi4Lsc570IkbdfMq6Zm11b0oE2pEWxNMLhTjkilgQeLVKkHyK-Vfl-aPe95V8Xk8YpMoZjYT6K3-DZXfcoDbTY55cDnutZcDujamgYKOuuT7s5dLhIM2l4NW4ISB-7P0-_iCtHMwWnq3YyHN7gJABzJfKCwX_Jw_ujq--QQ-0mPjO5W0aNcvVDSx_NbtoY")
    appid = models.CharField(max_length=200,default="F8BQRJffnkOm79ae8BCE5w")
