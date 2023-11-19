from django import forms
from .models import Puntointeres

class PuntointeresForm(forms.ModelForm):
    class Meta:
        model = Puntointeres
        fields = ['latitud', 'longitud', 'nombre']

    def __init__(self, *args, **kwargs):
        super(PuntointeresForm, self).__init__(*args, **kwargs)
        self.fields['latitud'].widget.attrs.update({'class': 'form-control', 'style': 'display:none;'})
        self.fields['latitud'].label = ''
        self.fields['longitud'].widget.attrs.update({'class': 'form-control', 'style': 'display:none;'})
        self.fields['longitud'].label = ''
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})


