from django import forms
from .models import Dueno
from usuario.forms import UsuarioForm

class DuenoForm(UsuarioForm):
    class Meta(UsuarioForm.Meta):
        model = Dueno
        fields = UsuarioForm.Meta.fields + ['estacionamientos', 'imagen_dueno']