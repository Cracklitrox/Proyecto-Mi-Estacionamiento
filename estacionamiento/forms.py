from django import forms
from .models import *
from dueno.models import Dueno

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['id_dueno', 'direccion', 'disponible', 'tarifahora', 'observaciones']

    id_dueno = forms.ModelChoiceField(
        queryset=Dueno.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(min_length=3, max_length=10, required=True)
    tarifahora = forms.IntegerField(min_value=1, required=True)
    observaciones = forms.CharField(min_length=5, max_length=250, required=False)

    def __init__(self, *args, **kwargs):
        super(EstacionamientoForm, self).__init__(*args, **kwargs)
        
        # Personalizar la apariencia de los campos
        self.fields['id_dueno'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['tarifahora'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})

class CasillaForm(forms.ModelForm):
    class Meta:
        model = Casilla
        fields = ['posicion','disponible']

    def __init__(self, *args, **kwargs):
        super(CasillaForm, self).__init__(*args, **kwargs)