from django import forms
from .models import Tarjetacredito

class TarjetacreditoForm(forms.ModelForm):
    numero = forms.CharField(widget=forms.TextInput(attrs={'data-inputmask': "'mask': '9999-9999-9999-9999'"}))
    cvv = forms.CharField(widget=forms.TextInput(attrs={"type": "password", "maxlength": "3"}))

    class Meta:
        model = Tarjetacredito
        fields = ['numero', 'fechavencimiento', 'nombre_titular', 'cvv', 'id_banco']
        widgets = {
            "fechavencimiento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
        labels = {
            'numero': 'Numero Tarjeta',
            'fechavencimiento': 'Fecha de Vencimiento',
            'nombre_titular': 'Nombre del Titular',
            'cvv': 'CVV',
            'id_banco': 'Banco',
        }