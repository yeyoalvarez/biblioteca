from django.contrib import admin
from .models import *

# Register your models here.
# al colocar los modelos aqui luego se ven en el administrador
#barra de busqueda

class buscadoarLibros(admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'lugar_impresion']
    list_display = ['titulo', 'autor']

admin.site.register(libro, buscadoarLibros)
admin.site.register(archivo)
admin.site.register(temas)
admin.site.register(idioma)