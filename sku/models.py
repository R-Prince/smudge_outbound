from django.db import models


# Scrumble Products
class Product(models.Model):
    sku_code = models.CharField(max_length=10, null=False, blank=False)
    upc = models.IntegerField(null=False, blank=False)
    barcode = models.IntegerField(max_length=14, null=False, blank=False)
    outer_barcode = models.IntegerField(max_length=14, null=False, blank=False)
    upp = models.IntegerField(null=False, blank=False)
    cpp = models.IntegerField(null=False, blank=False)
    cs_per_layer = models.IntegerField(null=False, blank=False)
    layer = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.sku_code
