from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from .models import Sale
import json

def is_farm_manager(user):
    return user.groups.filter(name='Farm_Manager').exists()

# GET all sales records
@user_passes_test(is_farm_manager)
def sales_list(request):
    if request.method == 'GET':
        sales = Sale.objects.all()
        data = [{'id': s.id, 'date': s.date, 'quantity': s.quantity, 'description': s.description} for s in sales]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET single sale record
@user_passes_test(is_farm_manager)
def sale_detail(request, id):
    if request.method == 'GET':
        sale = get_object_or_404(Sale, id=id)
        data = {
            'id': sale.id,
            'date': sale.date,
            'quantity': sale.quantity,
            'description': sale.description
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST new sale record
@csrf_exempt
@user_passes_test(is_farm_manager)
def create_sale(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_sale = Sale.objects.create(
                date=data['date'],
                quantity=data['quantity'],
                description=data['description']
            )
            return JsonResponse({'success': f"Sale record created successfully."}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: date, quantity, description'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# PUT update sale record
@csrf_exempt
@user_passes_test(is_farm_manager)
def update_sale(request, id):
    if request.method == 'PUT':
        sale = get_object_or_404(Sale, id=id)
        data = json.loads(request.body)
        try:
            sale.date = data.get('date', sale.date)
            sale.quantity = data.get('quantity', sale.quantity)
            sale.description = data.get('description', sale.description)
            sale.save()
            return JsonResponse({'success': f"Sale record '{sale.id}' updated successfully."})
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Valid fields: date, quantity, description'}, status=400)
    else:
        return JsonResponse({'error': 'Only PUT requests are supported for this endpoint.'}, status=405)

# DELETE sale record
@csrf_exempt
@user_passes_test(is_farm_manager)
def delete_sale(request, id):
    if request.method == 'DELETE':
        sale = get_object_or_404(Sale, id=id)
        sale.delete()
        return JsonResponse({'success': f"Sale record '{sale.id}' deleted successfully."})
    else:
        return JsonResponse({'error': 'Only DELETE requests are supported for this endpoint.'}, status=405)
