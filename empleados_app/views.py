from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losEmpleados=Empleados.objects.all()

    return render(request,"gestionarEmp.html", {"misempleados":losEmpleados})

def registrarEmp(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre_empleado=request.POST["txtnombre"]
    id_producto=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    id_cliente=request.POST["txtdireccion"]
    id_venta=request.POST["txtpuesto"]
    fecha_contratacion=request.POST["txtfecha"]
    guardarVenta=Empleados.objects.create(id_empleado=id_empleado,nombre_empleado=nombre_empleado ,id_producto=id_producto,  correo_electronico=correo_electronico, id_cliente=id_cliente,id_venta=id_venta,fecha_contratacion=fecha_contratacion)
    return redirect("Empleados")

def seleccionarEmp(request,id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmp.html", {"misempleados": empleados})

def editarEmp(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre_empleado=request.POST["txtnombre"]
    id_producto=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    id_cliente=request.POST["txtdireccion"]
    id_venta=request.POST["txtpuesto"]
    fecha_contratacion=request.POST["txtfecha"]
    
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.id_empleado=id_empleado
    empleados.nombre_empleado=nombre_empleado
    empleados.id_producto=id_producto
    empleados.correo_electronico=correo_electronico
    empleados.id_cliente=id_cliente
    empleados.id_venta=id_venta
    empleados.fecha_contratacion=fecha_contratacion
    empleados.save()
    return redirect("Empleados")

def borrarEmp(request, id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.delete()

    return redirect("Empleados")