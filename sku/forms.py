from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'sku_code', 'upc',
            'barcode', 'outer_barcode', 'upp',
            'cpp', 'cs_per_layer', 'layer')


def __init__(self, *args, **kwargs):
    """ Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field"""

    super().__init__(*args, **kwargs)
    placeholders = {
        'sku_code': 'SKU Code',
        'upc': 'Units per Case',
        'barcode': 'Barcode',
        'outer_barcode': 'Outercase Barcode',
        'upp': 'Units per Pallet',
        'cpp': 'Cases per Pallet',
        'cs_per_pallet': 'Cases per Pallet',
        'layer': 'Layers per pallet',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'input-field'
        self.fields[field].label = False
