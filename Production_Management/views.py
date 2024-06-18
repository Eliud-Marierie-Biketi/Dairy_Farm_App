from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Production
import json

# GET all production records
def production_list(request):
    if request.method == 'GET':
        productions = Production.objects.all()
        data = [{'id': p.id, 'date': p.date, 'shift': p.shift, 'liters': p.liters, 'density': p.density, 'prompts': p.prompts} for p in productions]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET single production record
def production_detail(request, id):
    if request.method == 'GET':
        production = get_object_or_404(Production, id=id)
        data = {
            'id': production.id,
            'date': production.date,
            'shift': production.shift,
            'liters': production.liters,
            'density': production.density,
            'prompts': production.prompts
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST new production record
@csrf_exempt
def create_production(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_production = Production.objects.create(
                date=data['date'],
                shift=data['shift'],
                liters=data['liters'],
                density=data['density'],
                prompts=data['prompts']
            )
            return JsonResponse({'success': f"Production record created successfully."}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: date, shift, liters, density, prompts'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# PUT update production record
@csrf_exempt
def update_production(request, id):
    if request.method == 'PUT':
        production = get_object_or_404(Production, id=id)
        data = json.loads(request.body)
        try:
            production.date = data.get('date', production.date)
            production.shift = data.get('shift', production.shift)
            production.liters = data.get('liters', production.liters)
            production.density = data.get('density', production.density)
            production.prompts = data.get('prompts', production.prompts)
            production.save()
            return JsonResponse({'success': f"Production record '{production.id}' updated successfully."})
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Valid fields: date, shift, liters, density, prompts'}, status=400)
    else:
        return JsonResponse({'error': 'Only PUT requests are supported for this endpoint.'}, status=405)

# DELETE production record
@csrf_exempt
def delete_production(request, id):
    if request.method == 'DELETE':
        production = get_object_or_404(Production, id=id)
        production.delete()
        return JsonResponse({'success': f"Production record '{production.id}' deleted successfully."})
    else:
        return JsonResponse({'error': 'Only DELETE requests are supported for this endpoint.'}, status=405)
