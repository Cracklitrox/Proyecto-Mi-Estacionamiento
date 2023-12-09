from django import forms
from usuario.models import ClienteProfile

class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = ClienteProfile
        fields = ['vehiculos', 'tarjetas', 'telefono']