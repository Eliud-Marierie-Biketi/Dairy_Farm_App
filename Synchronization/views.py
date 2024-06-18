from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import QueuedAction, SynchronizationLog
import json

@csrf_exempt
@login_required
def queue_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            action = QueuedAction.objects.create(
                action_type=data['action_type'],
                model_name=data['model_name'],
                data=data['data'],
                user=request.user
            )
            return JsonResponse({'success': f"Action {action.action_type} queued for model {action.model_name}"}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: action_type, model_name, data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

@login_required
def synchronize_data(request):
    if request.method == 'POST':
        queued_actions = QueuedAction.objects.filter(user=request.user).order_by('timestamp')
        results = []

        for action in queued_actions:
            model = apps.get_model(action.model_name)
            try:
                if action.action_type == 'CREATE':
                    obj = model.objects.create(**action.data)
                    results.append({'action': 'CREATE', 'model': action.model_name, 'id': obj.id})
                elif action.action_type == 'UPDATE':
                    obj = model.objects.get(id=action.data['id'])
                    for key, value in action.data.items():
                        setattr(obj, key, value)
                    obj.save()
                    results.append({'action': 'UPDATE', 'model': action.model_name, 'id': obj.id})
                elif action.action_type == 'DELETE':
                    obj = model.objects.get(id=action.data['id'])
                    obj.delete()
                    results.append({'action': 'DELETE', 'model': action.model_name, 'id': action.data['id']})
                action.delete()
            except Exception as e:
                results.append({'error': str(e), 'action': action.action_type, 'model': action.model_name, 'data': action.data})

        SynchronizationLog.objects.create(
            user=request.user,
            details=json.dumps(results)
        )

        return JsonResponse({'results': results}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)
