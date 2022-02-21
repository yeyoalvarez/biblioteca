from django.contrib import admin
from .models import *

# Register your models here.
# al colocar los modelos aqui luego se ven en el administrador

admin.site.register(libro)
admin.site.register(archivo)
