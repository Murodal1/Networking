from django.db import models
from product.models import Product


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
