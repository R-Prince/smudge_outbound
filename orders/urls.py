from django.urls import path
from . import views

urlpatterns = [
    path('orders/create_order', views.create_order, name='create_order')
]
