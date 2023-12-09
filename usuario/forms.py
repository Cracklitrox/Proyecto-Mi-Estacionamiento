from django import forms
from .models import Contacto, Usuario
from django.core.exceptions import ValidationError



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)

    class Meta:
        model = Usuario
        fields = ['run', 'dv_run', 'nombre', 'appaterno', 'apmaterno',
                'nombre_usuario', 'email', 'telefono', 'direccion', 
                'vehiculos', 'tarjetas_credito', 'id_comuna'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden, intentelo nuevamente.")

        user = self.instance
        user.set_password(password1)
        return cleaned_data
    
    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise ValidationError("El nombre de usuario ya existe, intente con otro nombre.")
        return nombre_usuario
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("El email ya existe, intente con otro correo.")
        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if Usuario.objects.filter(telefono=telefono).exists():
            raise ValidationError("El teléfono ya existe, intentelo con otro numero.")
        return telefono