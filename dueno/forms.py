from django import forms
from usuario.models import DuenoProfile

class DuenoProfileForm(forms.ModelForm):

    class Meta:
        model = DuenoProfile
        fields = ['run','dv_run','estacionamientos'
                  ,'telefono','id_comuna']






