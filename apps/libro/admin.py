from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
# al colocar los modelos aqui luego se ven en el administrador
#barra de busqueda

# caracteristicas para importar
class libroResource(resources.ModelResource):
    class Meta:
        model = libro
        fields = ('signatura')

class personalizarLibros(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['titulo','id',]
    # usar las caracteristicas definidas en libroResource
    resource_class = libroResource
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
    search_fields = ['id','titulo','autor__nombre']
    readonly_fields = ['id']


# class ordenarCargaLibros(admin.ModelAdmin):
#     fields = ['']


admin.site.register(libro, personalizarLibros)
admin.site.register(persona)
admin.site.register(archivo)
admin.site.register(temas)
admin.site.register(idioma)