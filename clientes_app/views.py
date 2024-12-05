from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    lasClientes=Clientes.objects.all()

    return render(request,"gestionarClientes.html", {"misclientes":lasClientes})

def registrarCliente(request):
    id_cliente=request.POST["txtid_cliente"] 
    nombre_cliente=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    correo_electronico=request.POST["txtcorreo"]
    fecha_registro=request.POST["txtfecha"]
    id_venta=request.POST["txtcliente"]
    fecha_nacimiento=request.POST["txtedad"]
    guardarVenta=Clientes.objects.create(id_cliente=id_cliente, nombre_cliente=nombre_cliente,direccion=direccion,correo_electronico=correo_electronico, fecha_registro=fecha_registro, id_venta=id_venta, fecha_nacimiento=fecha_nacimiento)
    return redirect("Clientes")

def seleccionarCliente(request,id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misclientes": clientes})

def editarCliente(request):
    id_cliente=request.POST["txtid_cliente"] 
    nombre_cliente=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    correo_electronico=request.POST["txtcorreo"]
    fecha_registro=request.POST["txtfecha"]
    id_venta=request.POST["txtcliente"]
    fecha_nacimiento=request.POST["txtedad"]

    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.id_cliente=id_cliente
    clientes.nombre_cliente=nombre_cliente
    clientes.direccion=direccion
    clientes.correo_electronico=correo_electronico
    clientes.fecha_registro=fecha_registro
    clientes.id_venta=id_venta
    clientes.fecha_nacimiento=fecha_nacimiento
    clientes.save()
    return redirect("Clientes")

def borrarCliente(request, id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.delete()

    return redirect("Clientes")