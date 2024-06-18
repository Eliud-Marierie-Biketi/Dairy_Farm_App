from django.urls import path
from . import views

urlpatterns = [
    path('queue_action/', views.queue_action, name='queue_action'),
    path('synchronize_data/', views.synchronize_data, name='synchronize_data'),
]
