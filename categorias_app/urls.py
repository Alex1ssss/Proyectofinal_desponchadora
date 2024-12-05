from django.urls import path
from categorias_app import views

urlpatterns = [
    path("Categorias", views.inicio_vistaCategorias, name="Categoria"),
    path("registrarCat/", views.registrarCat, name="registrarCat"),
    path("seleccionarCat/<id_categoria>", views.seleccionarCat, name="seleccionarCat"),
    path("editarCat/", views.editarCat, name="editarCat"),
    path("borrarCat/<id_categoria>", views.borrarCat, name="borrarCat")
    ]
