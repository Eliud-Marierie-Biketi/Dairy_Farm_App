from django.urls import path
from . import views

urlpatterns = [
    # GET all inventory items
    path('inventory_list/', views.inventory_list, name='inventory_list'),

    # GET single inventory item
    path('inventory_detail/<str:item_id>/', views.inventory_detail, name='inventory_detail'),
    
    # POST new inventory item
    path('create_inventory/', views.create_inventory, name='create_inventory'),
    
    # PUT update inventory item
    path('update_inventory/<str:item_id>/', views.update_inventory, name='update_inventory'),
    
    # DELETE inventory item
    path('delete_inventory/<str:item_id>/', views.delete_inventory, name='delete_inventory'),
]
