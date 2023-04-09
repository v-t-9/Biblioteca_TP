from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('agregar_libro/', views.agregar_libro, name="agregar_libro"),
    path('eliminar_libro/', views.eliminar_libro, name="eliminar_libro"),
    path('agregar_autor/', views.agregar_autor, name="agregar_autor"),
    path('eliminar_autor/', views.eliminar_autor, name="eliminar_autor"),
]