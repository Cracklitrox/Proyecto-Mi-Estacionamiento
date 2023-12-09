from django import forms
from .models import Puntointeres

class PuntointeresForm(forms.ModelForm):
    class Meta:
        model = Puntointeres
        fields = ['latitud', 'longitud', 'nombre']

    latitud = forms.CharField(required=True,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    longitud = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly'})) 
    nombre = forms.CharField(required=True, min_length=3, max_length=15)

    def __init__(self, *args, **kwargs):
        super(PuntointeresForm, self).__init__(*args, **kwargs)
        self.fields['latitud'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitud'].widget.attrs.update({'class': 'form-control' })
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})