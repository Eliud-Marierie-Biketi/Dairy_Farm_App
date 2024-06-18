from django.db import models
from Cattle_Management.models import Cattle

class AIDetails(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    other_info = models.TextField()

    def __str__(self):
        return f"AI Detail for {self.cattle.name}"
