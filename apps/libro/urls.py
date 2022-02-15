from django.urls import path
from .views import crearLibro

urlpatterns = [
    path('crear_libro/',crearLibro, name='crear_libro')
]