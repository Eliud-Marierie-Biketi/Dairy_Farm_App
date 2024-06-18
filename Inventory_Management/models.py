from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
