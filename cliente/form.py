from django import forms
from usuario.models import ClienteProfile

class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = ClienteProfile
        fields = ['run','dv_run','vehiculos',
                  'tarjetas_credito','telefono','calificacion_promedio_cliente',
                  'id_comuna']