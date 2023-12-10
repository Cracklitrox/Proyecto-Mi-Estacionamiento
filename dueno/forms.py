from django import forms
from usuario.models import DuenoProfile
from usuario.forms import UserForm

class DuenoForm(UserForm):
    estacionamientos = forms.IntegerField(required=True)
    class Meta(UserForm.Meta):
        widgets = {
            'es_cliente': forms.HiddenInput(),
            'es_dueno': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.es_dueno = True
        if commit:
            user.save()
            DuenoProfile.objects.create(user=user, estacionamientos=self.cleaned_data['estacionamientos'])
        return user