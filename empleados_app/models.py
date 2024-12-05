from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleado = models.PositiveIntegerField(primary_key=True)
    nombre_empleado= models.CharField(max_length=20)
    id_producto=models.PositiveIntegerField()
    correo_electronico=models.EmailField(max_length=20)
    id_cliente=models.PositiveIntegerField()
    id_venta= models.PositiveIntegerField()
    fecha_contratacion=models.DateField()


    def __str__(self):
        return self.id_empleado