from django.shortcuts import render, redirect
from .models import Proveedores
# Create your views here.

def inicio_vistaProveedores(request):
    losProveedores=Proveedores.objects.all

    return render(request,"gestionarPro.html", {"misproveedores":losProveedores})

def registrarPro(request):
    id_proveedor=request.POST["txtid_proveedor"]
    nombre_proveedor=request.POST["txtnombre"]
    telefono_proveedor=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    contacto_principal=request.POST["txtprincipal"]
    guardarVenta=Proveedores.objects.create(id_proveedor=id_proveedor,nombre_proveedor=nombre_proveedor ,telefono_proveedor=telefono_proveedor,  correo_electronico=correo_electronico, direccion=direccion,contacto_principal=contacto_principal)
    return redirect("Proveedores")

def seleccionarPro(request,id_proveedor):
    proveedores=Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarPro.html", {"misproveedores": proveedores})

def editarPro(request):
    id_proveedor=request.POST["txtid_proveedor"]
    nombre_proveedor=request.POST["txtnombre"]
    telefono_proveedor=request.POST["txttelefono"]
    correo_electronico=request.POST["txtcorreo"]
    direccion=request.POST["txtdireccion"]
    contacto_principal=request.POST["txtprincipal"]
    
    proveedores=Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.id_proveedor=id_proveedor
    proveedores.nombre_proveedor=nombre_proveedor
    proveedores.telefono_proveedor=telefono_proveedor
    proveedores.correo_electronico=correo_electronico
    proveedores.direccion=direccion
    proveedores.contacto_principal=contacto_principal
    proveedores.save()
    return redirect("Proveedores")

def borrarPro(request, id_proveedor):
    proveedores=Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.delete()

    return redirect("Proveedores")