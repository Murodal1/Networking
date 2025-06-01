from django.db import models
from location.models import Location
from customer.models import Customer
from inventory.models import Inventory


class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    hire_date = models.DateField()
    position = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Store(models.Model):
    office_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.office_name}"





