from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = (
        'sku_code', 'upc', 'barcode', 'outer_barcode', 'upp',
        'cpp', 'cs_per_layer', 'layer')

    list_display = ('sku_code', 'upc', 'barcode', 'outer_barcode', 'upp',
                    'cpp', 'cs_per_layer', 'layer')


admin.site.register(Product, ProductAdmin)
