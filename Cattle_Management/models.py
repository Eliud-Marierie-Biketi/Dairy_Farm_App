from django.db import models

class Cattle(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='cattle_photos/')
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Procedure(models.Model):
    PROCEDURE_TYPES = [
        ('Dehorning', 'Dehorning'),
        ('Deworming', 'Deworming'),
        ('Vaccination', 'Vaccination'),
        ('Treatment', 'Treatment'),
        ('Spraying', 'Spraying'),
        ('Multi-Vitamin', 'Multi-Vitamin'),
        ('Iron Injection', 'Iron Injection'),
    ]
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    procedure_type = models.CharField(max_length=20, choices=PROCEDURE_TYPES)
    date = models.DateField()
    method = models.CharField(max_length=100, blank=True)  # For dehorning
    drug = models.CharField(max_length=100, blank=True)  # For deworming, vaccination, treatment, spraying
    next_due_date = models.DateField(blank=True, null=True)  # For deworming, vaccination, periodic procedures
    veterinary_name = models.CharField(max_length=100)
    chemical_used = models.CharField(max_length=100, blank=True)  # For spraying

    def __str__(self):
        return f"{self.procedure_type} for {self.cattle.name} on {self.date}"
