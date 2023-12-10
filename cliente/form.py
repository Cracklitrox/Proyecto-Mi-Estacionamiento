from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuario.models import UsuarioProfile, User

class ClienteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'apmaterno', 'telefono', 'email', 'username', 'password1', 'password2')
        widgets = {
            'es_cliente': forms.HiddenInput(),
            'es_dueno': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
            'calificacion_promedio_cliente': forms.HiddenInput(),
        }
   

class UsuarioProfileForm(forms.ModelForm):
    class Meta:
        model = UsuarioProfile
        fields = ('run', 'dv_run', 'id_comuna')