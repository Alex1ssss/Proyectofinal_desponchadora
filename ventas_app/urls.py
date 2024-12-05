from django.urls import path
from ventas_app import views

urlpatterns = [
    path("Venta", views.inicio_vistaVentas, name="Venta"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<id_venta>", views.seleccionarVenta, name="seleccionarVenta"),
    path("editarVentas/", views.editarVentas, name="editarVentas"),
    path("borrarVenta/<id_venta>", views.borrarVenta, name="borrarVenta")
    ]
