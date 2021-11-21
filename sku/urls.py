from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('products/create_sku', views.create_sku, name='create_sku'),
]
