from django.urls import path
from . import views

urlpatterns = [
    path('listar_cursos/', views.Listar_cursos, name='listar_cursos'),
    path('crear_curso/', views.Crear_curso, name='crear_curso'),
    path('editar_curso/<int:curso_id>/', views.Editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:curso_id>/', views.Eliminar_curso, name='eliminar_curso')
]