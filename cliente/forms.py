from django import forms
from .models import Cliente
from usuario.forms import UsuarioForm

class ClienteForm(UsuarioForm):
    class Meta(UsuarioForm.Meta):
        model = Cliente
        fields = UsuarioForm.Meta.fields + ['imagen_cliente']