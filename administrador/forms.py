import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from transaccion_pago.models import Banco, Tarjetacredito
from usuario.models import Comuna, Provincia, Region, Contacto
from cliente.models import Cliente
from dueno.models import Dueno
from .models import CustomUser

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    imagen = forms.ImageField(required=False)
    nombre = forms.CharField(max_length=30, required=True, help_text='Nombre')
    apellidos = forms.CharField(max_length=30, required=True, help_text='Apellidos')
    nivel_permiso = forms.IntegerField(min_value=0, max_value=5, required=True)

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
            raise ValidationError('El nivel de permiso debe estar entre 0 y 5.')
        return nivel_permiso
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
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

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not (1000000 <= len(str(run)) <= 99999999):
            raise ValidationError('La longitud del run estar entre 1.000.000 y 99.999.999 caracteres.')
        return run

    # def clean_dv_run(self):
    #     dv_run = self.cleaned_data.get('dv_run')
    #     if not dv_run:
    #         raise ValidationError('El campo Dígito Verificador del Run no puede estar vacío.')
    #     if dv_run not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'K'}:
    #         raise ValidationError('El Dígito Verificador del Run debe ser un número entre 0 y 9 o la letra K.')
    #     return dv_run

    # def clean_correoelectronico(self):
    #     correo_electronico = self.cleaned_data.get('correoelectronico')
    #     if not correo_electronico:
    #         raise ValidationError('El campo Correo Electrónico no puede estar vacío.')
    #     patron_correo = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    #     if not patron_correo.match(correo_electronico):
    #         raise ValidationError('El formato del Correo Electrónico no es válido.')
    #     nombre_usuario = correo_electronico.split('@')[0]
    #     if len(nombre_usuario) < 5:
    #         raise ValidationError('El nombre de usuario en el Correo Electrónico debe tener al menos 5 caracteres.')
    #     return correo_electronico

    # def clean_telefono(self):
    #     telefono = self.cleaned_data.get('telefono')
    #     if not telefono:
    #         raise ValidationError('El campo Teléfono no puede estar vacío.')
    #     if not telefono.isdigit():
    #         raise ValidationError('El teléfono debe contener solo dígitos.')
    #     if len(telefono) < 8:
    #         raise ValidationError('El teléfono debe tener al menos 8 dígitos.')
    #     return telefono

    # def clean_nombreusuario(self):
    #     nombre_usuario = self.cleaned_data.get('nombreusuario')
    #     if not nombre_usuario:
    #         raise ValidationError('El campo Nombre de Usuario no puede estar vacío.')
    #     if not re.match("^[a-zA-Z0-9]+$", nombre_usuario):
    #         raise ValidationError('El nombre de usuario debe contener solo letras y números.')
    #     if len(nombre_usuario) < 5:
    #         raise ValidationError('El nombre de usuario debe tener al menos 5 caracteres.')
    #     return nombre_usuario

    # def clean_contrasena(self):
    #     contrasena = self.cleaned_data.get('contrasena')
    #     if not contrasena:
    #         raise ValidationError('El campo Contraseña no puede estar vacío.')
    #     if not re.match("^[a-zA-Z0-9]+$", contrasena):
    #         raise ValidationError('La contraseña debe contener solo letras y números.')
    #     if len(contrasena) < 5:
    #         raise ValidationError('La contraseña debe tener al menos 5 caracteres.')
    #     return contrasena

    # def clean_pnombre(self):
    #     pnombre = self.cleaned_data.get('pnombre')
    #     if not pnombre:
    #         raise ValidationError('El campo Primer Nombre del Cliente no puede estar vacío.')
    #     if not pnombre.isalpha():
    #         raise ValidationError('El Primer Nombre del Cliente solo debería contener caracteres alfabéticos.')
    #     if len(pnombre) < 5:
    #         raise ValidationError('El Primer Nombre del Cliente debe tener al menos 5 caracteres.')
    #     return pnombre

    # def clean_snombre(self):
    #     snombre = self.cleaned_data.get('snombre')
    #     if not snombre:
    #         raise ValidationError('El campo Segundo Nombre del Cliente no puede estar vacío.')
    #     if not snombre.isalpha():
    #         raise ValidationError('El Segundo Nombre del Cliente solo debería contener caracteres alfabéticos.')
    #     if len(snombre) < 5:
    #         raise ValidationError('El Segundo Nombre del Cliente debe tener al menos 5 caracteres.')
    #     return snombre

    # def clean_appaterno(self):
    #     appaterno = self.cleaned_data.get('appaterno')
    #     if not appaterno:
    #         raise ValidationError('El campo Primer Apellido del Cliente no puede estar vacío.')
    #     if not appaterno.isalpha():
    #         raise ValidationError('El Primer Apellido del Cliente solo debería contener caracteres alfabéticos.')
    #     if len(appaterno) < 5:
    #         raise ValidationError('El Primer Apellido del Cliente debe tener al menos 5 caracteres.')
    #     return appaterno

    # def clean_apmaterno(self):
    #     apmaterno = self.cleaned_data.get('apmaterno')
    #     if not apmaterno:
    #         raise ValidationError('El campo Segundo Apellido del Cliente no puede estar vacío.')
    #     if not apmaterno.isalpha():
    #         raise ValidationError('El Segundo Apellido del Cliente solo debería contener caracteres alfabéticos.')
    #     if len(apmaterno) < 5:
    #         raise ValidationError('El Segundo Apellido del Cliente debe tener al menos 5 caracteres.')
    #     return apmaterno

    # def clean_direccion(self):
    #     direccion = self.cleaned_data.get('direccion')
    #     if not direccion:
    #         raise ValidationError('La Direccion del Cliente no puede estar vacío.')
    #     if len(direccion) < 5:
    #         raise ValidationError('La Direccion del Cliente debe tener al menos 5 caracteres.')
    #     return direccion

    # def clean_id_tarjetacredito(self):
    #     id_tarjeta_credito = self.cleaned_data.get('id_tarjetacredito')
    #     if not id_tarjeta_credito:
    #         raise ValidationError('Debe seleccionar una Tarjeta de Crédito.')
    #     return id_tarjeta_credito

    # def clean_id_banco(self):
    #     id_banco = self.cleaned_data.get('id_banco')
    #     if not id_banco:
    #         raise ValidationError('Debe seleccionar un Banco.')
    #     return id_banco

    # def clean_id_comuna(self):
    #     id_comuna = self.cleaned_data.get('id_comuna')
    #     if not id_comuna:
    #         raise ValidationError('Debe seleccionar una Comuna.')
    #     return id_comuna

class DuenoForm(forms.ModelForm):

    class Meta:
        model = Dueno
        fields = "__all__"