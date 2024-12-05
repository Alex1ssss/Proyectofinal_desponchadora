from django.db import models

# Create your models here.

class Categorias(models.Model):
    id_categoria = models.PositiveIntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)
    descripcion_categoria=models.CharField(max_length=20)
    fecha_creacion=models.DateField()
    años_activo=models.PositiveIntegerField()
    id_proveedor= models.PositiveIntegerField()
    id_producto=models.PositiveIntegerField()
    
    def __str__(self):
        return self.id_categoria