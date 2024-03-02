# models.py

from django.contrib.auth.models import User
from django.db import models

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

class Farm(models.Model):
    farm_id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,related_name='farms')
    farm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    total_acres = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.farm_name
    
class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE,related_name='crops')  # Change 'farm_id' to 'farm'
    crop_name = models.CharField(max_length=255)
    planting_date = models.DateField()
    harvesting_date = models.DateField()
    yield_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return self.crop_name
    

    
class Livestock(models.Model):
    livestock_id = models.AutoField(primary_key=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    livestock_type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    health_status = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
        return f"{self.livestock_type} - {self.farm.farm_name}"

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    expense_type = models.CharField(max_length=20, default='')  # Add default value
    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, default=1) 

    def __str__(self):
        return f"Expense {self.expense_id} - {self.description}"