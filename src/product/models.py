from django.db import models
from supply.models import Supplier


class Product(models.Model):
    cloth_name = models.CharField(max_length=100)
    spoiled_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=80)
    colour = models.CharField(max_length=80)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)




