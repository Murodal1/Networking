from django.db import models
from product.models import Product


class Order(models.Model):
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)





class Item_order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

