from django.urls import path
from . import views

urlpatterns = [
    # GET all AI details
    path('ai_list/', views.ai_list, name='ai_list'),

    # GET single AI detail
    path('ai_detail/<str:serial_number>/', views.ai_detail, name='ai_detail'),
    
    # POST new AI detail
    path('create_ai/', views.create_ai, name='create_ai'),
    
    # PUT update AI detail
    path('update_ai/<str:serial_number>/', views.update_ai, name='update_ai'),
    
    # DELETE AI detail
    path('delete_ai/<str:serial_number>/', views.delete_ai, name='delete_ai'),
]
