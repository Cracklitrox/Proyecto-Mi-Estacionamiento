from django.shortcuts import render

# Create your views here.
def indexCliente(request):
    return render(request,'indexCliente.html')

def pagoCliente(request):
    return render(request,'pagoCliente.html')

def registroCliente(request):
    return render(request,'registroCliente.html')