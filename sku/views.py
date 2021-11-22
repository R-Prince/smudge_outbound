from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from .models import Product
from .forms import ProductForm


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
            'cs_per_layer': request.POST['cs_per_layer'],
            'layer': request.POST['layer']
        }
        product = ProductForm(form_data)
        if product.is_valid():
            product.save()
            return redirect(reverse('products'))
    
    form = ProductForm()
    template = 'sku/create_sku.html'
    context = {
        'form': form
    }
    return render(request, template, context)


# View Scrumble Products
def products(request):
    return render(request, 'sku/products.html')

# Edit existing Scrumble Products
# Delete Scrumble Products
