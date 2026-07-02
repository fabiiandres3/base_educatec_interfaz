from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cursos/', blank=True, null=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre