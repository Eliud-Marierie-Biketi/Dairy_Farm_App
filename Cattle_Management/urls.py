from django.urls import path
from . import views

urlpatterns = [
    # GET all cattle
    path('cattle_list', views.cattle_list, name='cattle_list'),

    # GET, PUT, DELETE single cattle
    path('cattle_detail/<str:serial_number>/', views.cattle_detail, name='cattle_detail'),
    
    # POST new cattle
    path('create_cattle', views.create_cattle, name='create_cattle'),
    
    # PUT update cattle
    path('cattle/<str:serial_number>/update/', views.update_cattle, name='update_cattle'),
    
    # DELETE cattle
    path('cattle/<str:serial_number>/delete/', views.delete_cattle, name='delete_cattle'),
]
