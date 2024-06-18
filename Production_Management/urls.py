from django.urls import path
from . import views

urlpatterns = [
    # GET all production records
    path('production_list/', views.production_list, name='production_list'),

    # GET single production record
    path('production_detail/<int:id>/', views.production_detail, name='production_detail'),
    
    # POST new production record
    path('create_production/', views.create_production, name='create_production'),
    
    # PUT update production record
    path('update_production/<int:id>/', views.update_production, name='update_production'),
    
    # DELETE production record
    path('delete_production/<int:id>/', views.delete_production, name='delete_production'),
]
