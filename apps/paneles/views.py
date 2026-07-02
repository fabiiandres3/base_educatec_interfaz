from django.shortcuts import render

# Create your views here.
# apps/paneles/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# ─────────────────────────────────────────
# PROFESOR
# ─────────────────────────────────────────

def dashboard_profesor(request):
    return render(request, 'paneles/profesor/dashboard_profesor.html')

def cursos_profesor(request):
    return render(request, 'paneles/profesor/cursos_profesor.html')

def calificaciones_profesor(request):
    return render(request, 'paneles/profesor/calificaciones_profesor.html')

def asistencia_profesor(request):
    return render(request, 'paneles/profesor/asistencia_profesor.html')

def historial_asistencia(request):
    return render(request, "paneles/profesor/historial_asistencia.html")

def guardar_asistencia(request):
    return render(request, "paneles/profesor/guardar_asistencia.html")

def configuracion_profesor(request):
    return render(request, 'paneles/profesor/configuracion_profesor.html')


# ─────────────────────────────────────────
# ESTUDIANTE
# ─────────────────────────────────────────


def dashboard_estudiante(request):
    return render(request, 'paneles/estudiante/dashboard_estudiante.html')

def materias_estudiante(request):
    return render(request, 'paneles/estudiante/materias_estudiante.html')


def calificaciones_estudiante(request):
    return render(request, 'paneles/estudiante/calificaciones_estudiante.html')


def asistencia_estudiante(request):
    return render(request, 'paneles/estudiante/asistencia_estudiante.html')


def logros_estudiante(request):
    return render(request, 'paneles/estudiante/logros_estudiante.html')


def configuracion_estudiante(request):
    return render(request, 'paneles/estudiante/configuracion_estudiante.html')