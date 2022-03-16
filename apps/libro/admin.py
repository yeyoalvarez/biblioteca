from django.contrib import admin
from .models import *

# Register your models here.
# al colocar los modelos aqui luego se ven en el administrador
#barra de busqueda

class personalizarLibros(admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'lugar_impresion']
    list_display = ['titulo', 'autor']
    # ordenar como se vera al cargar
    fieldsets = (
        ( 'Seccion 1',{
            'fields':('signatura','fecha_carga','tema_libro',
            'idioma_libro')
        }),
        ( 'Datos Libro',{
            'fields':('titulo','autor','autor2','editorial','coleccion',
            'edicion', 'isbn', 'lugar_impresion','anho_impresion',
            'notas')
        }),
    )

# class ordenarCargaLibros(admin.ModelAdmin):
#     fields = ['']

class autocompletar(admin.ModelAdmin):
  search_fields = ['nombre']

admin.site.register(persona, autocompletar)
admin.site.register(persona)
admin.site.register(libro,personalizarLibros)
admin.site.register(archivo)
admin.site.register(temas)
admin.site.register(idioma)