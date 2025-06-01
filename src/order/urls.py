from django.urls import path, include
from .views import orders

urlpatterns = [
    path('', orders, name='orders'),
]