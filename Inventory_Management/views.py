from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Inventory
import json

# GET all inventory items
def inventory_list(request):
    if request.method == 'GET':
        items = Inventory.objects.all()
        data = [{'item_id': item.item_id, 'name': item.name, 'quantity': item.quantity, 'description': item.description} for item in items]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET single inventory item
def inventory_detail(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Inventory, item_id=item_id)
        data = {
            'item_id': item.item_id,
            'name': item.name,
            'quantity': item.quantity,
            'description': item.description
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST new inventory item
@csrf_exempt
def create_inventory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_item = Inventory.objects.create(
                item_id=data['item_id'],
                name=data['name'],
                quantity=data['quantity'],
                description=data['description']
            )
            return JsonResponse({'success': f"Inventory item '{new_item.item_id}' created successfully."}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: item_id, name, quantity, description'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# PUT update inventory item
@csrf_exempt
def update_inventory(request, item_id):
    if request.method == 'PUT':
        item = get_object_or_404(Inventory, item_id=item_id)
        data = json.loads(request.body)
        try:
            item.item_id = data.get('item_id', item.item_id)
            item.name = data.get('name', item.name)
            item.quantity = data.get('quantity', item.quantity)
            item.description = data.get('description', item.description)
            item.save()
            return JsonResponse({'success': f"Inventory item '{item.item_id}' updated successfully."})
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Valid fields: item_id, name, quantity, description'}, status=400)
    else:
        return JsonResponse({'error': 'Only PUT requests are supported for this endpoint.'}, status=405)

# DELETE inventory item
@csrf_exempt
def delete_inventory(request, item_id):
    if request.method == 'DELETE':
        item = get_object_or_404(Inventory, item_id=item_id)
        item.delete()
        return JsonResponse({'success': f"Inventory item '{item.item_id}' deleted successfully."})
    else:
        return JsonResponse({'error': 'Only DELETE requests are supported for this endpoint.'}, status=405)
