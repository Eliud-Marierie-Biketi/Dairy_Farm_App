from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AIDetails
import json

# GET all AI details
def ai_list(request):
    if request.method == 'GET':
        ai_details = AIDetails.objects.all()
        data = [{'serial_number': ai.serial_number, 'name': ai.name, 'origin': ai.origin, 'other_info': ai.other_info} for ai in ai_details]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET single AI detail
def ai_detail(request, serial_number):
    if request.method == 'GET':
        ai = get_object_or_404(AIDetails, serial_number=serial_number)
        data = {
            'serial_number': ai.serial_number,
            'name': ai.name,
            'origin': ai.origin,
            'other_info': ai.other_info
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST new AI detail
@csrf_exempt
def create_ai(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_ai = AIDetails.objects.create(
                serial_number=data['serial_number'],
                name=data['name'],
                origin=data['origin'],
                other_info=data['other_info']
            )
            return JsonResponse({'success': f"AI detail '{new_ai.serial_number}' created successfully."}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: serial_number, name, origin, other_info'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# PUT update AI detail
@csrf_exempt
def update_ai(request, serial_number):
    if request.method == 'PUT':
        ai = get_object_or_404(AIDetails, serial_number=serial_number)
        data = json.loads(request.body)
        try:
            ai.serial_number = data.get('serial_number', ai.serial_number)
            ai.name = data.get('name', ai.name)
            ai.origin = data.get('origin', ai.origin)
            ai.other_info = data.get('other_info', ai.other_info)
            ai.save()
            return JsonResponse({'success': f"AI detail '{ai.serial_number}' updated successfully."})
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Valid fields: serial_number, name, origin, other_info'}, status=400)
    else:
        return JsonResponse({'error': 'Only PUT requests are supported for this endpoint.'}, status=405)

# DELETE AI detail
@csrf_exempt
def delete_ai(request, serial_number):
    if request.method == 'DELETE':
        ai = get_object_or_404(AIDetails, serial_number=serial_number)
        ai.delete()
        return JsonResponse({'success': f"AI detail '{ai.serial_number}' deleted successfully."})
    else:
        return JsonResponse({'error': 'Only DELETE requests are supported for this endpoint.'}, status=405)
