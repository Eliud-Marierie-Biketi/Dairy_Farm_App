from django.urls import path
from . import views

urlpatterns = [
    # GET all sales records
    path('sales_list/', views.sales_list, name='sales_list'),

    # GET single sale record
    path('sale_detail/<int:id>/', views.sale_detail, name='sale_detail'),
    
    # POST new sale record
    path('create_sale/', views.create_sale, name='create_sale'),
    
    # PUT update sale record
    path('update_sale/<int:id>/', views.update_sale, name='update_sale'),
    
    # DELETE sale record
    path('delete_sale/<int:id>/', views.delete_sale, name='delete_sale'),
]
