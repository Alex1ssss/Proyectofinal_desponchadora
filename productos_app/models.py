from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto = models.PositiveIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    fecha_ingreso=models.DateField()
    precio_producto=models.PositiveBigIntegerField()
    descripcion_producto=models.CharField(max_length=20)
    categoria_producto= models.CharField(max_length=20)
    stock= models.PositiveIntegerField()
    
    def __str__(self):
        return self.id_producto