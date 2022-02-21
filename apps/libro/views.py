from django.shortcuts import render, redirect
from .forms import libroForm
from .models import libro

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

def listarLibro(request):
    libros = libro.objects.all()
    return  render(request,'libro/listar_libros.html',{'libros':libros})