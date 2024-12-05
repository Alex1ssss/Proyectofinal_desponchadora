from django.db import models

# Create your models here.

class Ventas(models.Model):
    id_venta = models.PositiveIntegerField(primary_key=True)
    id_cliente = models.PositiveIntegerField()
    fecha_venta=models.DateField()
    total_venta=models.DecimalField(max_digits=6,decimal_places=2)
    id_producto=models.PositiveIntegerField()
    id_empleado= models.PositiveIntegerField()
    cantidad_productos = models.PositiveIntegerField()


    def __str__(self):
        return self.id_venta