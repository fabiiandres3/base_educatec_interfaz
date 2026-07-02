from django.contrib import admin
from .models import Usuario, Roles

# Register your models here.

admin.site.register(Roles)
admin.site.register(Usuario)