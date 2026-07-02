# apps/user/decorators.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def docente_o_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if request.user.rol.nombre.lower() in ["docente", "administrador"]:
            return view_func(request, *args, **kwargs)

        messages.error(request, "No tienes permisos para acceder a esta página.")
        return redirect("inicio")  # Cambia "inicio" por la vista que desees

    return _wrapped_view