# Generated by Django 5.1 on 2024-12-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre_empleado', models.CharField(max_length=20)),
                ('id_producto', models.PositiveIntegerField()),
                ('correo_electronico', models.EmailField(max_length=20)),
                ('id_cliente', models.PositiveIntegerField()),
                ('id_venta', models.PositiveIntegerField()),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
    ]
