import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto
from .models import CustomUser

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    imagen = forms.ImageField(required=False)
    nombre = forms.CharField(max_length=30, required=True, help_text='Nombre')
    apellidos = forms.CharField(max_length=30, required=True, help_text='Apellidos')
    nivel_permiso = forms.IntegerField(min_value=0, max_value=3, required=True)

    class Meta:
        model = CustomUser
        fields = ['nombre', 'apellidos', 'username', 'email', 'password1', 'password2', 'nivel_permiso', 'imagen']
    
    def clean_username(self):
        nombreusuario = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=nombreusuario).exists():
            raise ValidationError('Este nombre de usuario ya está registrado.')
        return nombreusuario

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return email

    def clean_nivel_permiso(self):
        nivel_permiso = self.cleaned_data.get('nivel_permiso')
        if not (0 <= nivel_permiso <= 5):
            raise ValidationError('El nivel de permiso debe estar entre 0 y 3.')
        return nivel_permiso
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
            # if user.nivel_permiso == 1:
            #     group = Group.objects.get(name='AdministradorNivelPermiso1')
            #     user.groups.add(group)
            # elif user.nivel_permiso == 2:
            #     group = Group.objects.get(name='AdministradorNivelPermiso2')
            #     user.groups.add(group)
            # elif user.nivel_permiso == 3:
            #     group = Group.objects.get(name='AdministradorNivelPermiso3')
            #     user.groups.add(group)
        return user

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = "__all__"

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre del banco no puede estar vacío.')
        elif not nombre.isalpha():
            raise ValidationError('El nombre del banco solo debería contener caracteres alfabéticos.')
        return nombre

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
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre de la comuna no puede estar vacío.')
        elif not nombre.isalpha():
            raise ValidationError('El nombre de la comuna solo debería contener caracteres alfabéticos.')
        return nombre

class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = Provincia
        fields = "__all__"
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre de la provincia no puede estar vacío.')
        elif not nombre.isalpha():
            raise ValidationError('El nombre de la provincia solo debería contener caracteres alfabéticos.')
        return nombre

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = "__all__"
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre de la region no puede estar vacío.')
        elif not nombre.isalpha():
            raise ValidationError('El nombre de la region solo debería contener caracteres alfabéticos.')
        return nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('El nombre del contacto no puede estar vacío.')
        elif not nombre.isalpha():
            raise ValidationError('El nombre del contacto solo debería contener caracteres alfabéticos.')
        elif len(nombre) < 5:
            raise ValidationError('El nombre del contacto debe tener al menos 5 caracteres.')
        return nombre

    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        if not correo_electronico:
            raise ValidationError('El correo electrónico del contacto no puede estar vacío.')
        elif len(correo_electronico) < 5:
            raise ValidationError('El correo electrónico debe tener al menos 5 caracteres.')
        return correo_electronico

    def clean_tipo_consulta(self):
        tipo_consulta = self.cleaned_data.get('tipo_consulta')
        if tipo_consulta not in [0, 1, 2, 3]:
            raise ValidationError('Tipo de consulta no válido.')
        return tipo_consulta

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if not mensaje:
            raise ValidationError('El mensaje del contacto no puede estar vacío.')
        elif len(mensaje) < 5:
            raise ValidationError('El mensaje debe tener al menos 5 caracteres.')
        return mensaje

    def clean_avisos(self):
        avisos = self.cleaned_data.get('avisos')
        if avisos is None:
            raise ValidationError('Debe elegir entre activar avisos o no.')
        return avisos