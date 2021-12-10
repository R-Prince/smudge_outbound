import csv
from django.shortcuts import render


# Create a new order
def create_order(request):
    return render(request, 'orders/create_order.html')
