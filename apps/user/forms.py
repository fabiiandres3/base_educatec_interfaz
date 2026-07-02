from django import forms


class UsuarioForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=100
    )

    first_name = forms.CharField(
        label="Nombre",
        max_length=100
    )

    last_name = forms.CharField(
        label="Apellido",
        max_length=100
    )

    email = forms.EmailField(
        label="Correo electrónico"
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario"
    )

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )