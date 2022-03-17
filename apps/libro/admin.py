from django.contrib import admin
from .models import *

# Register your models here.
# al colocar los modelos aqui luego se ven en el administrador
#barra de busqueda

class personalizarLibros(admin.ModelAdmin):
    list_display = ['id','titulo']
    # ordenar como se vera al cargar
    fieldsets = (
        ( 'Seccion 1',{
            'fields':('id','signatura','fecha_carga','tema_libro',
            'idioma_libro')
        }),
        ( 'Datos Libro',{
            'fields':('titulo','autor','editorial','coleccion',
            'edicion', 'isbn', 'lugar_impresion','anho_impresion',
            'notas')
        }),
    )
    search_fields = ['nombre']
    readonly_fields = ['id']


# class ordenarCargaLibros(admin.ModelAdmin):
#     fields = ['']


admin.site.register(libro, personalizarLibros)
admin.site.register(persona)
admin.site.register(archivo)
admin.site.register(temas)
admin.site.register(idioma)