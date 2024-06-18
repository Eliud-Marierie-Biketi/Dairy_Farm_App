from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Payment of {self.amount} by {self.customer.name} on {self.date}"

class Sale(models.Model):
    date = models.DateField()
    quantity_calves = models.FloatField()  # Quantity given to calves
    quantity_sold = models.FloatField()  # Quantity sold
    quantity_csr = models.FloatField()  # Quantity for CSR
    quantity_staff = models.FloatField()  # Quantity consumed by staff
    spillage = models.FloatField()
    spoilage = models.FloatField()

    def __str__(self):
        return f"Sales on {self.date}"
