from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import HiddenInput
from .models import Contacto, User

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class UsuarioRegistrationForm(UserCreationForm):
    # Añade campos adicionales según sea necesario
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
            'pnombre', 'snombre', 'apellidos', 'is_cliente',
            'is_dueno', 'is_staff'
        ]
        widgets = {
            'is_cliente': forms.HiddenInput(),
            'is_dueno': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
        }
