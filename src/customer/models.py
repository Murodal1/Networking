from django.db import models
from location.models import Location
from order.models import Order


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

