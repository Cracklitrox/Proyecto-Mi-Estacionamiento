from django.shortcuts import render

# Create your views here.
def indexDueno(request):
    return render(request,'indexDueno.html')

def cargando(request):
    return render(request,'cargando.html')

def estacionamientos(request):
    return render(request,'estacionamientos.html')