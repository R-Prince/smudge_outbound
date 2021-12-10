from django.db import models
from sku.models import Product


# Pah Products and Prices
class Pah(models.Model):
    sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku_code = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    channel = models.CharField(max_length=100, null=False, blank=False)
    sku_type = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.sku_code
