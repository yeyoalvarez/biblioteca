from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
    buscar = request.GET.get('buscar')
    libros = libro.objects.all()

    if buscar:
        libros = libros.objects.filter(
            Q(titulo_icontains = buscar)
        ).distinct

    return  render(request,'libro/listar_libros.html',{'libros':libros})

def editarLibros(request,id):
    libro_form = None
    error = None
    try:
        libroEditar = libro.objects.get(id=id)
        if request.method == 'GET':
            libro_form = libroForm(instance=libroEditar)
        else:
            libro_form = libroForm(request.POST, instance=libroEditar)
            if libro_form.is_valid():
                libro_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'libro/crear_libro.html',{'libro_form':libro_form,'error':error})

