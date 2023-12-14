from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import HiddenInput
from .models import Contacto, User, DuenoProfile, ClienteProfile

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'apmaterno', 'telefono', 'email', 'username', 'password1', 'password2')
        widgets = {
            'es_cliente': HiddenInput(),
            'es_dueno': HiddenInput(),
            'is_staff': HiddenInput(),
        }

class UsuarioProfileForm (forms.ModelForm):
    class Meta:
        model = DuenoProfile
        fields = ('run','dv_run','id_comuna')
        widgets = {
            'calificacion': HiddenInput(),
        }
        
class ClienteProfileForm (forms.ModelForm):
    class Meta:
        model = ClienteProfile
        fields = ('run','dv_run','id_comuna')
        widgets = {
            'calificacion': HiddenInput(),
        }