from django import forms
from .models import libro


class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo', 'autor', 'editorial', 'coleccion', 'edicion',
                  'isbn', 'lugar_impresion', 'notas', 'anho_impresion']
