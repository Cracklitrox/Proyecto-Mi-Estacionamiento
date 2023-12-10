from django import forms
from .models import *

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['direccion', 'disponible', 'tarifahora', 'observaciones']

    direccion = forms.CharField(min_length=3, max_length=10, required=True)
    tarifahora = forms.IntegerField(min_value=1, required=True)
    observaciones = forms.CharField(min_length=5, max_length=250, required=False)

    def __init__(self, *args, **kwargs):
        super(EstacionamientoForm, self).__init__(*args, **kwargs)
        
        # Personalizar la apariencia de los campos
        # self.fields['id_dueno'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['tarifahora'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})