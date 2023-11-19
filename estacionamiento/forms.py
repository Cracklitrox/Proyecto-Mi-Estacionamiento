from django import forms

from .models import Estacionamiento

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['id_dueno', 'direccion', 'disponible', 'tarifahora', 'observaciones']

    def __init__(self, *args, **kwargs):
        super(EstacionamientoForm, self).__init__(*args, **kwargs)

        # Configurar el valor predeterminado de disponible como False   
        self.fields['disponible'].initial = False
        
        # Personalizar la apariencia de los campos
        self.fields['id_dueno'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['tarifahora'].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control'})
        
    # ... otros campos y configuraciones ...