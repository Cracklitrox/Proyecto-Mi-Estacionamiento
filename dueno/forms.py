from django import forms
from usuario.models import DuenoProfile

class DuenoProfileForm(forms.ModelForm):

    class Meta:
        model = DuenoProfile
        fields = ['run','dv_run','estacionamientos',
                  'calificacion_promedio_dueno','telefono','id_comuna']






