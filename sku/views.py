from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from .models import Product


# Create new Scrumble Products
def create_sku(request):
    if request.method == 'POST':
        form_data = {
            'sku_code': request.POST['sku_code'],
            'upc': request.POST['upc'],
            'barcode': request.POST['barcode'],
            'outer_barcode': request.POST['outer_barcode'],
            'upp': request.POST['upp'],
            'cpp': request.POST['cpp'],
            'cs_per_pallet': request.POST['cs_per_pallet'],
            'layer': request.POST['layer']
        }
        product = Product(form_data)
        if product.is_valid():
            product.save()
            return redirect(reverse('products'))
    return render(request, 'sku/create_sku.html')


# View Scrumble Products
def products(request):
    return render(request, 'sku/products.html')

# Edit existing Scrumble Products
# Delete Scrumble Products
