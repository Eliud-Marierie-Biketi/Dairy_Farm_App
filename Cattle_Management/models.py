from django.db import models

class Cattle(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='cattle_photos/')
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True, blank=True)

    def generate_serial_number(self):
        # Get the first two letters of the farm name (assuming it's stored somewhere)
        farm_name = 'RFMB'  # Replace this with actual farm name retrieval logic
        farm_prefix = farm_name[:2].upper()

        # Get the first two letters of the cattle's name
        cattle_prefix = self.name[:2].upper()

        # Get the last two digits of the year of birth
        

        # Count the number of existing cattle objects to generate auto-incremented number
        count = Cattle.objects.count() + 1
        auto_number = str(count).zfill(3)  # Pad with leading zeros to ensure 3-digit number

        # Concatenate all parts to form the serial number
        serial_number = f"{farm_prefix}{cattle_prefix}{auto_number}"
        return serial_number

    def save(self, *args, **kwargs):
        # Generate serial number if not provided
        if not self.serial_number:
            self.serial_number = self.generate_serial_number()
        super().save(*args, **kwargs)

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
