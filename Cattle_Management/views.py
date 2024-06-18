from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cattle
import json

# GET all cattle
def cattle_list(request):
    if request.method == 'GET':
        cattle = Cattle.objects.all()
        data = [{'name': c.name, 'date_of_birth': c.date_of_birth} for c in cattle]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET single cattle
def cattle_detail(request, serial_number):
    if request.method == 'GET':
        cattle = get_object_or_404(Cattle, serial_number=serial_number)
        data = {
            'name': cattle.name,
            'date_of_birth': cattle.date_of_birth,
            'father': cattle.father,
            'mother': cattle.mother
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST new cattle
@csrf_exempt
def create_cattle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_cattle = Cattle.objects.create(
                name=data['name'],
                date_of_birth=data['date_of_birth'],
                father=data['father'],
                mother=data['mother']
            )
            return JsonResponse({'success': f"Cattle '{new_cattle.name}' created successfully."}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: name, date_of_birth, father, mother'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# PUT update cattle
@csrf_exempt
def update_cattle(request, serial_number):
    if request.method == 'PUT':
        cattle = get_object_or_404(Cattle, serial_number=serial_number)
        data = json.loads(request.body)
        try:
            cattle.name = data.get('name', cattle.name)
            cattle.date_of_birth = data.get('date_of_birth', cattle.date_of_birth)
            cattle.father = data.get('father', cattle.father)
            cattle.mother = data.get('mother', cattle.mother)
            cattle.save()
            return JsonResponse({'success': f"Cattle '{cattle.name}' updated successfully."})
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Valid fields: name, date_of_birth, father, mother'}, status=400)
    else:
        return JsonResponse({'error': 'Only PUT requests are supported for this endpoint.'}, status=405)

# DELETE cattle
@csrf_exempt
def delete_cattle(request, serial_number):
    if request.method == 'DELETE':
        cattle = get_object_or_404(Cattle, serial_number=serial_number)
        cattle.delete()
        return JsonResponse({'success': f"Cattle '{cattle.name}' deleted successfully."})
    else:
        return JsonResponse({'error': 'Only DELETE requests are supported for this endpoint.'}, status=405)
