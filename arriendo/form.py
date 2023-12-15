from django import forms
from .models import Arriendo
from estacionamiento.models import *
from django.forms.widgets import HiddenInput

class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = ['id_estacionamiento', 'id_user', 'horainicio', 'horafin', 'preciototal', 'calificacioncliente', 'calificaciondueno']
        widgets = {
            'horainicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'horafin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'id_estacionamiento': HiddenInput(),
            'id_user': HiddenInput(),
            'calificacioncliente': HiddenInput(),
            'calificaciondueno': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        id_estacionamiento = kwargs.pop('id_estacionamiento', None)
        id_user = kwargs.pop('id_user', None)
        preciototal = kwargs.pop('preciototal', None)

        super(ArriendoForm, self).__init__(*args, **kwargs)

        if id_estacionamiento:
            self.fields['id_estacionamiento'].initial = id_estacionamiento
        if id_user:
            self.fields['id_user'].initial = id_user
        if preciototal:
            self.fields['preciototal'].initial = preciototal

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})