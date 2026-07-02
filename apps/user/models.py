from django.contrib.auth.models import AbstractUser
from django.db import models


class Roles(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    rol = models.ForeignKey(
        Roles,
        on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"