from django.db import models
from Cattle_Management.models import Cattle

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Production(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.CharField(max_length=20, choices=[('AM', 'AM'), ('PM', 'PM'), ('Noon', 'Noon'), ('Other', 'Other')])
    liters = models.FloatField()
    density = models.FloatField()
    prompt = models.TextField(blank=True)  # For increased/reduced production prompts

    def __str__(self):
        return f"Production for {self.cattle.name} on {self.date}"
