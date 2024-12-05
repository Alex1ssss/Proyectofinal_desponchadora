from django.urls import path
from app_base import views

urlpatterns = [
    #inicio desponchadora
    path('', views.inicio),
]
