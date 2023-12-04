from django import forms
from django.core.exceptions import ValidationError
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto
from cliente.models import Cliente
from dueno.models import Dueno

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = "__all__"

class TarjetacreditoForm(forms.ModelForm):
    class Meta:
        model = Tarjetacredito
        fields = '__all__'
        widgets = {
            "fechavencimiento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        try:
            int(numero)
        except (ValueError, TypeError):
            raise ValidationError('El número de tarjeta debe ser un valor entero.')
        
        if not (12 <= len(str(numero)) <= 16):
            raise ValidationError('La longitud del número de tarjeta debe estar entre 12 y 16 caracteres.')
        
        return numero

    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        try:
            int(cvv)
        except (ValueError, TypeError):
            raise ValidationError('El CVV debe ser un valor entero.')

        if not (cvv is not None and len(str(cvv)) == 3):
            raise ValidationError('El CVV debe tener exactamente 3 dígitos.')
        
        return cvv

    def clean_fechavencimiento(self):
        fechavencimiento = self.cleaned_data.get('fechavencimiento')
        return fechavencimiento

    def __init__(self, *args, **kwargs):
        super(TarjetacreditoForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['fechavencimiento'].initial = kwargs['instance'].fechavencimiento.strftime("%Y-%m-%d")

class ComunaForm(forms.ModelForm):

    class Meta:
        model = Comuna
        fields = "__all__"

class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = Provincia
        fields = "__all__"

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = "__all__"

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"

class DuenoForm(forms.ModelForm):

    class Meta:
        model = Dueno
        fields = "__all__"