from django.shortcuts import render, redirect, get_object_or_404
from .forms import CursosForm
from .models import Cursos

# Create your views here.


def Listar_cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'admin/cursos/cursos.html', {'cursos': cursos})

def Crear_curso(request):
    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursosForm()
    return render(request, 'admin/cursos/crear_curso.html', {'form': form})

def Editar_curso(request, curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == 'POST':
        form = CursosForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursosForm(instance=curso)

    return render(request, 'admin/cursos/editar_curso.html', {'form': form, 'curso':curso})

def Eliminar_curso(request, curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    curso.delete()
    return redirect('listar_cursos')