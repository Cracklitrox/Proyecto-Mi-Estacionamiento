from django import forms
from .models import Arriendo
from dueno.models import Dueno
from cliente.models import Cliente
from estacionamiento.models import *


class arriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['id_cliente','id_dueno','id_estacionamiento','horainicio','horafin','preciototal']
        widgets = {
            'horainicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'horafin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(arriendoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
