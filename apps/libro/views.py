from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def crearLibro(request):
    if request.method == 'POST':
        libro_form = libroForm(request.POST)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('index')
    else:
        libro_form = libroForm()
    return render(request,'libro/crear_libro.html',{'libro_form':libro_form})

