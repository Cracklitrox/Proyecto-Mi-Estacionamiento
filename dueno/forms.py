from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuario.models import UsuarioProfile, User

class DuenoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'apmaterno', 'telefono', 'email', 'username', 'password1', 'password2')
        widgets = {
            'es_cliente': forms.HiddenInput(),
            'es_dueno': forms.HiddenInput(),
            'is_staff': forms.HiddenInput(),
            'calificacion_promedio_dueno': forms.HiddenInput(),
        }

class UsuarioProfileForm(forms.ModelForm):
    class Meta:
        model = UsuarioProfile
        fields = ('run', 'dv_run', 'id_comuna')

# class DuenoForm(UserCreationForm):
    
#     class Meta:
#         model : User  
#         fields = []
#         widgets = {
#             'es_cliente': forms.HiddenInput(),
#             'es_dueno': forms.HiddenInput(),
#             'is_staff': forms.HiddenInput(),
#         }

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.es_dueno = True
#         if commit:
#             user.save()
#             DuenoProfile.objects.create(user=user)
#         return user