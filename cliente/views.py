from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def pago(request):
    return render(request,'pago.html')

def registro(request):
    return render(request,'registro.html')