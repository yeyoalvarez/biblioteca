from django.urls import path
from .views import crearLibro, listarLibro

urlpatterns = [
    path('crear_libro/',crearLibro, name='crear_libro'),
    path('listar_libros/',listarLibro, name='listar_libros')
]