from django import forms
from .models import autor, libro

class autorForm(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['nombre_completo']

class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo','fecha_impresion','editorial','coleccion','edicion',
                  'isbn','lugar_impresion','notas']