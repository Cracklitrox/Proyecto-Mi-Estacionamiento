from django import forms
from .models import *
from django.forms.widgets import HiddenInput

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

               
    
class EstacionamientoForms(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = "__all__"
        widgets = {
            'id_dueno': HiddenInput(),
            'disponible': HiddenInput(),
            'id_puntoInteres': HiddenInput(),
        }


    def __init__(self, *args, **kwargs):
        super(EstacionamientoForms, self).__init__(*args, **kwargs)
        self.fields['direccion'].widget.attrs.update({'class': 'form-control mb-'})
        self.fields['disponible'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['tarifahora'].widget.attrs.update({'class': 'form-control'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file'})

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente', 'id_marca', 'modelo']
        labels = {
            'id_marca': 'Marca'
        }
