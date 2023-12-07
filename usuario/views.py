from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.


# Funcion CONTACTO

def contacto(request):
    context = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje_correcto"] = "Se ha enviado correctamente el mensaje y contacto."
        else:
            context["form"] = formulario
            context["mensaje_incorrecto"] = "No se ha podido enviar correctamente el mensaje y contacto, intentelo nuevamente."
    return render(request, 'contacto.html', context)