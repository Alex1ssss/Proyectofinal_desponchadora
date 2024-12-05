from django.urls import path
from empleados_app import views

urlpatterns = [
    path("Empleados", views.inicio_vistaEmpleados, name="Empleados"),
    path("registrarEmp/", views.registrarEmp, name="registrarEmp"),
    path("seleccionarEmp/<id_empleado>", views.seleccionarEmp, name="seleccionarEmp"),
    path("editarEmp/", views.editarEmp, name="editarEmp"),
    path("borrarEmp/<id_empleado>", views.borrarEmp, name="borrarEmp")
    ]
