from django.urls import path
from . import views

urlpatterns = [
    path('clases/', views.Listar_Clases, name='clases'),
    path('clases/crear/', views.Crear_clase, name='crear_clase'),
    path('clases/editar/<int:clase_id>/', views.Editar_clase, name='editar_clase'),
    path('clases/eliminar/<int:clase_id>/', views.Eliminar_clase, name='eliminar_clase'),
]
