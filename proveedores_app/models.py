from django.db import models

# Create your models here.

class Proveedores(models.Model):
    id_proveedor = models.PositiveIntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=20)
    telefono_proveedor=models.PositiveBigIntegerField()
    correo_electronico=models.EmailField(max_length=20)
    direccion=models.CharField(max_length=20)
    contacto_principal= models.CharField(max_length=10)
    
    def __str__(self):
        return self.id_proveedor