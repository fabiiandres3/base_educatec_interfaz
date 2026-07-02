from django.shortcuts import render, redirect
from apps.user.models import Usuario, Roles
from apps.user.forms import UsuarioForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")


def prescolar(request):
    return render(request, "programas/prescolar.html")


def primaria(request):
    return render(request, "programas/primaria.html")


def secundaria(request):
    return render(request, "programas/secundaria.html")


def Registrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if Usuario.objects.filter(email=email).exists():
                form.add_error("email", "Ya existe un usuario con este correo.")
                return render(request, "login/registrar_usuario.html", {"form": form})

            if Usuario.objects.filter(username=username).exists():
                form.add_error("username", "Este usuario ya existe.")
                return render(request, "login/registrar_usuario.html", {"form": form})

            # Obtener el rol "usuario"
            rol_usuario = Roles.objects.get(nombre="usuario")

            user = Usuario(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                rol=rol_usuario,
            )

            user.set_password(password)
            user.save()

            return redirect("login")

    else:
        form = UsuarioForm()

    return render(request, "login/registrar_usuario.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Verificar el rol del usuario
                if user.rol:
                    rol = user.rol.nombre.lower()

                    if rol == "usuario":
                        return redirect("verificacion")

                    elif rol in ["docente", "administrador"]:
                        return redirect("dashboard")  # Nombre de la URL del panel docente

                # Si no tiene rol asignado
                return redirect("login")

            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")

    else:
        form = LoginForm()

    return render(request, "login/login.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("index")


def verificacion(request):
    if request.user.is_authenticated:
        return render(request, "login/verificacion.html")
    
def dashboard(request):
    return render(request, "admin/dashboard.html")
