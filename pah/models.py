from django.db import models
from sku.models import Product


# Pah Products and Prices
class Pah(models.Model):
    sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku_code = models.CharField(max_length=10, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    vat = models.IntegerField(max_length=14, null=False, blank=False)
    channel = models.IntegerField(max_length=14, null=False, blank=False)
    sku_type = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.sku
