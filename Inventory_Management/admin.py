from django.contrib import admin
from .models import Equipment, Inventory, RawMaterial

# Register your models here.

admin.site.register(Equipment)
admin.site.register(Inventory)
admin.site.register(RawMaterial)
