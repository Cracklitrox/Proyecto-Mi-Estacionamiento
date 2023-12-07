from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contacto, Usuario

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class UsuarioRegistrationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'run', 'dv_run', 'nombre', 'appaterno', 'apmaterno', 'email',
            'username', 'direccion', 'telefono', 'password1', 'password2',
            'vehiculos', 'tarjetas_credito', 'imagen', 
            'id_comuna',
        ]

    def clean_run(self):
        run = self.cleaned_data.get('run')
        # Lógica de validación del RUN si es necesario
        return run

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está registrado.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email