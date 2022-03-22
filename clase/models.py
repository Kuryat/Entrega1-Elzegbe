from django.db import models

# Create your models here.

class Musico(models.Model):
    nombre = models.CharField(max_length=20) 
    instrumento = models.CharField(max_length=30)
    
        
     
class Recitales(models.Model):
    ciudad = models.CharField(max_length=20) 
    nombre = models.CharField(max_length=30) 
    
    
class Banda(models.Model):
    nombre = models.CharField(max_length=20) 
    ciudad = models.CharField(max_length=20)
  
    def __str__(self):
        return f"Banda: {self.nombre} - Ciudad: {self.ciudad}"
    
