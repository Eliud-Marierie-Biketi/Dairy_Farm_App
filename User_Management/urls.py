from django.urls import path
from . import views

urlpatterns = [
    # Worker URLs
    path('worker_list/', views.worker_list, name='worker_list'),
    path('worker_detail/<str:username>/', views.worker_detail, name='worker_detail'),
    
    # Message URLs
    path('send_message/', views.send_message, name='send_message'),
    path('message_list/', views.message_list, name='message_list'),
    
    # Task Log URLs
    path('create_task_log/', views.create_task_log, name='create_task_log'),
]
