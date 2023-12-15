from django import forms
from .models import Tarjetacredito

class TarjetacreditoForm(forms.ModelForm):
    numero = forms.CharField(widget=forms.TextInput(attrs={'data-inputmask': "'mask': '9999-9999-9999-9999'"}))
    fechavencimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    cvv = forms.CharField(widget=forms.PasswordInput(), max_length=3)

    class Meta:
        model = Tarjetacredito
        fields = ['numero', 'fechavencimiento', 'nombre_titular', 'cvv', 'id_banco']
        labels = {
            'id_banco': 'Banco'
        }