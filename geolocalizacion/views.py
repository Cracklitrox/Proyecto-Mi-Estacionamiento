from django.shortcuts import render

# Create your views here.

def gps(request):
    return render (request, 'gps.html')
