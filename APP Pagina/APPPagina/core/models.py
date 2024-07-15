from django.db import models
from django.contrib.auth.models import User

class Beat(models.Model):
    idBeat= models.IntegerField(primary_key=True,verbose_name='Id del beat')
    nombreBeat= models.CharField(max_length=50, verbose_name='Nombre del Beat')
    descripcion= models.CharField(max_length=200, verbose_name='Descripcion del Beat')
    nombreColab= models.CharField(max_length=50, verbose_name='Nombre Colaboracion', blank=True)
    precioBeat= models.IntegerField(verbose_name='Precio Beat')
    imgenBeat= models.ImageField(upload_to='Beats/',null=True,blank=True)
    
    
    def __str__(self):
        return self.nombreBeat
    
    def getPrecio(self):
        return f"${self.precioBeat}"