from django.contrib import admin
from .models import Sale, Customer, Payment

# Register your models here.

admin.site.register(Sale)
admin.site.register(Customer)
admin.site.register(Payment)
