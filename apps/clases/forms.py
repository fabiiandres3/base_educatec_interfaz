from django import forms
from .models import Clases

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ['titulo', 'curso']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título'
            })
        }