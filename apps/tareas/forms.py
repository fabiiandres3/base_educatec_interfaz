from django import forms
from .models import Tareas, Pregunta


class TareasForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ["titulo", "descripcion", "fecha_entrega",'clase', 'curso']

        widgets = {
            "fecha_entrega": forms.DateInput(attrs={"type": "date"}),
            "descripcion": forms.Textarea(
                attrs={"rows": 1, "cols": -20, "class": "form-control"}
            ),
        }

class PreguntasForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['descripcion', 'tipo', 'puntaje']