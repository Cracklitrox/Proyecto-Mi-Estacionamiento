from django import forms
from usuario.models import ClienteProfile
from usuario.forms import UserForm

class ClienteForm(UserForm):
    class Meta(UserForm.Meta):
        widgets = {
            'es_cliente': forms.HiddenInput(),
            'es_dueno': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.es_cliente = True
        if commit:
            user.save()
            ClienteProfile.objects.create(user=user)
        return user