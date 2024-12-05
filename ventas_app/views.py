from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.

def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all()

    return render(request,"gestionarVentas.html", {"misventas":lasVentas})

def registrarVenta(request):
    id_venta=request.POST["txtventa"] 
    id_cliente=request.POST["txtcliente"]
    fecha_venta=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    id_producto=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    cantidad_productos=request.POST["txtestatus"]
    guardarVenta=Ventas.objects.create(id_venta=id_venta, fecha_venta=fecha_venta,total_venta=total_venta, id_cliente=id_cliente, id_producto=id_producto, id_empleado=id_empleado, cantidad_productos=cantidad_productos)
    return redirect("Venta")

def seleccionarVenta(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    return render(request, "editarVentas.html", {"misventas": ventas})

def editarVentas(request):
    id_venta=request.POST["txtventa"] 
    id_cliente=request.POST["txtcliente"]
    fecha_venta=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    id_producto=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    cantidad_productos=request.POST["txtestatus"]    
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.id_venta=id_venta
    ventas.id_cliente=id_cliente
    ventas.fecha_venta=fecha_venta
    ventas.total_venta=total_venta
    ventas.id_producto=id_producto
    ventas.id_empleado=id_empleado
    ventas.cantidad_productos=cantidad_productos
    ventas.save()
    return redirect("Venta")

def borrarVenta(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.delete()

    return redirect("Venta")