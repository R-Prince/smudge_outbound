from django.urls import path
from . import views

urlpatterns = [
    path('pah', views.pah, name='pah')
]
