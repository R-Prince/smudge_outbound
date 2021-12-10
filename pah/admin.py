from django.contrib import admin
from .models import Pah


class PahAdmin(admin.ModelAdmin):
    fields = ('sku', 'sku_code',
                'price', 'vat', 'channel',
                'sku_type')

    list_display = ('sku_code', 'price', 'channel',
                    'sku_type')


admin.site.register(Pah, PahAdmin)