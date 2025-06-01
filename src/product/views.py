from django.shortcuts import render
from .models import Product
from customer.models import Customer, Order

def products(request):
    products = Product.objects.select_related('supplier').all()
    product_count = products.count()
    customer = Customer.objects.count()
    orders = Order.objects.count()
    ctx = {
        'products': products,
        'product_count': product_count,
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'products.html', ctx)