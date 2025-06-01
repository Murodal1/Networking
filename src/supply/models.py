from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_name

