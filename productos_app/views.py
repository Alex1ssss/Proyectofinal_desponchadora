from django.shortcuts import render, redirect
from .models import Productos
# Create your views here.

def inicio_vistaProductos(request):
    losProductos=Productos.objects.all()

    return render(request,"gestionarProducto.html", {"misproductos":losProductos})

def registrarProducto(request):
    id_producto=request.POST["txtproducto"] 
    nombre_producto=request.POST["txtnombre"]
    fecha_ingreso=request.POST["txtfecha"]
    precio_producto=request.POST["txtprecio"]
    descripcion_producto=request.POST["txtdescripcion"]
    categoria_producto=request.POST["txtcategoria"]
    stock=request.POST["txtstock"]
    guardarVenta=Productos.objects.create(id_producto=id_producto, nombre_producto=nombre_producto, fecha_ingreso=fecha_ingreso,precio_producto=precio_producto, descripcion_producto=descripcion_producto, categoria_producto=categoria_producto, stock=stock)
    return redirect("Producto")

def seleccionarProducto(request,id_producto):
    productos=Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": productos})

def editarProducto(request):
    id_producto=request.POST["txtproducto"] 
    nombre_producto=request.POST["txtnombre"]
    fecha_ingreso=request.POST["txtfecha"]
    precio_producto=request.POST["txtprecio"]
    descripcion_producto=request.POST["txtdescripcion"]
    categoria_producto=request.POST["txtcategoria"]
    stock=request.POST["txtstock"]
    
    productos=Productos.objects.get(id_producto=id_producto)
    productos.id_producto=id_producto
    productos.nombre_producto=nombre_producto
    productos.precio_producto=precio_producto
    productos.fecha_ingreso=fecha_ingreso
    productos.descripcion_producto=descripcion_producto
    productos.categoria_producto=categoria_producto
    productos.stock=stock
    productos.save()
    return redirect("Producto")

def borrarProducto(request, id_producto):
    productos=Productos.objects.get(id_producto=id_producto)
    productos.delete()

    return redirect("Producto")