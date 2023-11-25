from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Estacionamiento
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cambiar_estado(request, estacionamiento_id):
    try:
        estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
        estacionamiento.cambiar_estado()
        return JsonResponse({'estado': estacionamiento.disponible})
    except Estacionamiento.DoesNotExist:
        return JsonResponse({'error': 'Estacionamiento no encontrado'}, status=404)
