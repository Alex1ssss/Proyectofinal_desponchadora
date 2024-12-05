from django.urls import path
from proveedores_app import views

urlpatterns = [
    path("Proveedores", views.inicio_vistaProveedores, name="Proveedores"),
    path("registrarPro/", views.registrarPro, name="registrarPro"),
    path("seleccionarPro/<id_proveedor>", views.seleccionarPro, name="seleccionarPro"),
    path("editarPro/", views.editarPro, name="editarPro"),
    path("borrarPro/<id_proveedor>", views.borrarPro, name="borrarPro")
    ]
