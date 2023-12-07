# from django import forms
# from .models import Arriendo
# from estacionamiento.models import *


# class ArriendoForm(forms.ModelForm):
#     # Añade id_estacionamiento_actual como campo

#     class Meta:
#         model = Arriendo
#         fields = ['id_estacionamiento', 'horainicio', 'horafin', 'preciototal','calificacioncliente','calificaciondueno']
#         widgets = {
#             'horainicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#             'horafin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }

#     def __init__(self, *args, **kwargs):
#         # Obtiene y elimina los valores personalizados del diccionario kwargs
#         id_estacionamiento = kwargs.pop('id_estacionamiento', None)
#         # id_dueno = kwargs.pop('id_dueno', None)
#         preciototal = kwargs.pop('preciototal', None)

#         # Llama al constructor del formulario con los argumentos restantes
#         super(ArriendoForm, self).__init__(*args, **kwargs)

#         # Configura los valores en los campos personalizados
#         if id_estacionamiento:
#             self.fields['id_estacionamiento'].initial = id_estacionamiento
#         if preciototal:
#             self.fields['preciototal'].initial = preciototal

#         for field_name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})