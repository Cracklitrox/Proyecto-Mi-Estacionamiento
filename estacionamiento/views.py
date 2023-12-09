from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# def cambiar_casilla(request, casilla_id):
#     try:
#         estacionamientoCasilla = EstacionamientoCasilla.objects.get(id=casilla_id)
#         estacionamientoCasilla.cambiar_casilla()
#         return JsonResponse({'estado': estacionamientoCasilla.disponible})
#     except EstacionamientoCasilla.DoesNotExist:
#         return JsonResponse({'error': 'EstacionamientoCasilla no encontrada'}, status=404)
