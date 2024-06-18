from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Admin, Worker, Message, Upload, TaskLog
import json

def is_manager(user):
    return user.is_superuser  # Assuming the farm manager is a superuser

# GET all workers
@login_required
@user_passes_test(is_manager)
def worker_list(request):
    if request.method == 'GET':
        workers = Worker.objects.all()
        data = [{'username': w.user.username, 'position': w.position, 'contact_info': w.contact_info} for w in workers]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# GET worker details
@login_required
@user_passes_test(is_manager)
def worker_detail(request, username):
    if request.method == 'GET':
        worker = get_object_or_404(Worker, user__username=username)
        data = {
            'username': worker.user.username,
            'position': worker.position,
            'contact_info': worker.contact_info,
            'uploads': [{'file': u.file.url, 'description': u.description, 'timestamp': u.timestamp} for u in worker.upload_set.all()],
            'task_logs': [{'task_description': t.task_description, 'date': t.date} for t in worker.tasklog_set.all()]
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST message
@csrf_exempt
@login_required
@user_passes_test(is_manager)
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            receiver = get_object_or_404(Admin, username=data['receiver'])
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                subject=data['subject'],
                body=data['body']
            )
            return JsonResponse({'success': f"Message sent to {receiver.username}"}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: receiver, subject, body'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)

# GET messages
@login_required
def message_list(request):
    if request.method == 'GET':
        messages = request.user.received_messages.all()
        data = [{'sender': m.sender.username, 'subject': m.subject, 'body': m.body, 'timestamp': m.timestamp} for m in messages]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are supported for this endpoint.'}, status=405)

# POST task log
@csrf_exempt
@login_required
@user_passes_test(is_manager)
def create_task_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            worker = get_object_or_404(Worker, user__username=data['worker'])
            task_log = TaskLog.objects.create(
                worker=worker,
                task_description=data['task_description'],
                date=data['date']
            )
            return JsonResponse({'success': f"Task log created for {worker.user.username}"}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid request body. Required fields: worker, task_description, date'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are supported for this endpoint.'}, status=405)
